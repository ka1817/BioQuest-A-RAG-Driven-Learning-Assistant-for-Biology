from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv
import os
import uvicorn

load_dotenv()

app = FastAPI(title="A RAG-Driven Learning Assistant for Biology")


from langchain.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.schema import Document, BaseRetriever
from sentence_transformers import CrossEncoder
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferWindowMemory
from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

loader = DirectoryLoader('data/', glob="**/*.pdf", show_progress=True, loader_cls=PyPDFLoader)
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
chunks = splitter.split_documents(documents)

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(chunks, embeddings)

GROQ_API_KEY = os.getenv('GROQ_API_KEY')
llm = ChatGroq(api_key=GROQ_API_KEY, model='llama-3.3-70b-versatile')

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful and knowledgeable biology tutor. Answer clearly and accurately. If the query is out of syllabus, just respond with 'Out of syllabus'."),
    ("human", "Context:\n{context}\n\nQuestion: {question}")
])

memory = ConversationBufferWindowMemory(
    memory_key="chat_history",
    return_messages=True,
    k=3
)

reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

def rerank_documents(query: str, retrieved_docs: List[Document]) -> List[Document]:
    docs_texts = [doc.page_content for doc in retrieved_docs]
    pairs = [(query, doc_text) for doc_text in docs_texts]
    scores = reranker.predict(pairs)
    sorted_docs = [doc for _, doc in sorted(zip(scores, retrieved_docs), key=lambda x: x[0], reverse=True)]
    return sorted_docs

class RerankRetriever(BaseRetriever, BaseModel):
    base_retriever: BaseRetriever
    top_k: int = 5

    def _get_relevant_documents(self, query: str) -> List[Document]:
        initial_docs = self.base_retriever.invoke(query)
        reranked_docs = rerank_documents(query, initial_docs)
        return reranked_docs[:self.top_k]

base_retriever = vectorstore.as_retriever(search_kwargs={"k": 10})
custom_retriever = RerankRetriever(base_retriever=base_retriever, top_k=5)

qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=custom_retriever,
    memory=memory,
    combine_docs_chain_kwargs={"prompt": prompt}
)


class QuestionInput(BaseModel):
    question: str

@app.post("/predict")
def predict(input: QuestionInput):
    result = qa_chain.invoke({"question": input.question})
    return {"answer": result["answer"]}


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=2000)
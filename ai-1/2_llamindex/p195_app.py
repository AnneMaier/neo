import os
from llama_index import GPTVectorStoreIndex, StorageContext, LLMPredictor, ServiceContext, LangchainEmbedding, SimpleDirectoryReader

from llama_index.vector_stores.faiss import FaissVectorStore
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import HuggingFaceEmbeddings
import faiss

document = SimpleDirectoryReader('data').load_data()
print("-" * 50)
print("documents loaded successfully")
print("-" * 50)

faiss_index = faiss.IndexFlatL2(384)
vector_store = FaissVectorStore(faiss_index)ㅔㅐㅐ
storage_context = StorageContext.from_defaults(vector_store=vector_store)
service_context = ServiceContext.from_defaults(
    llm_predictor = llm_predictor,
    embed_model = embed_model,
)

print("Faiss Index and Vector Store initialized successfully")
print("-" * 50)

index = GPTVectorStoreIndex.from_documents(
    documents = document,
    service_context = service_context,
    storage_context = storage_context,
)

index.storage_context.persist(persist_dir = "./storage")
print("Index created successfully")
print("-" * 50)


query_engine = index.as_query_engine()
print("Query Engine initialized successfully")
print("-" * 50)

query = "미코의 소꿉친구 이름은?"
response = query_engine.query(query)
print(f"Query: {query}", end="\n")
print(f"Response: {response}", end="\n")

print("-" * 50)
from llama_index import Document
from llama_index import GPTVectorStoreIndex


text = ['text1', 'text2','text3']

documents = [Document(text) for text in text]
print("-" * 50)
print("Documents: ", documents)
print("-" * 50)

index = GPTVectorStoreIndex.from_documents(documents)

print("-" * 50 )

print("index: ", index)

print("-" * 50)

for doc in documents:
    index.insert(doc)
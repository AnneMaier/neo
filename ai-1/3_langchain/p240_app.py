from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

with open("akazukin_all.txt") as f:
    text_all = f.read()


text_splitter = CharacterTextSplitter(
    chunk_size=300,
    separator="\n\n",
    chunk_overlap=20)

texts = text_splitter.split_text(text_all)

print("-" * 50)
print(len(texts))
for text in texts:
    print(text[:10], ":", len(text))

docsearch = FAISS.from_texts(
    texts = texts, 
    embedding = OpenAIEmbeddings())

qa_chain = RetrievalQA.from_chain_type(
    llm = OpenAI(
        model="gpt-3.5-turbo-instruct",
        temperature=0
    ),
    chain_type="stuff",
    retriever=docsearch.as_retriever(),
)

print("-" * 50)
query = "미코의 소꿉친구의 이름은?"

result = qa_chain({"query" :query})
print("-" * 50)
print(result)
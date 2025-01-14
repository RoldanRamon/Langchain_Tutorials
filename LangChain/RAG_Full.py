from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.runnables import RunnablePassthrough

loader = PyPDFLoader('rag_vs_fine_tuning.pdf')
data = loader.load()

# Split the document using RecursiveCharacterTextSplitter
splitter = RecursiveCharacterTextSplitter(
separators=["\n\n", "\n", " ", ""],
chunk_size=300,
chunk_overlap=50)   
docs = splitter.split_documents(data) 

# Embed the documents in a persistent Chroma vector database
embedding_function = OpenAIEmbeddings(api_key='OPENAI_API_TOKEN', model='text-embedding-3-small')
vectorstore = Chroma.from_documents (
    docs,
    embedding=embedding_function,
    persist_directory=os.getcwd()
)

# Configure the vector store as a retriever
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k":2}
)

# Create a chain to link retriever, prompt_template, and llm
rag_chain = ({"context": retriever, "question": RunnablePassthrough()}
            | prompt_template
            | llm)

# Invoke the chain
response = rag_chain.invoke("Which popular LLMs were considered in the paper?")
print(response.content)
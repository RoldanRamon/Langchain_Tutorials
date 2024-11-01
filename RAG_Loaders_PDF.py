# Import library
from langchain_community.document_loaders import PyPDFLoader

# Create a document loader for rag_vs_fine_tuning.pdf
loader = PyPDFLoader("./Material/chapter3.pdf")

# Load the document
data = loader.load()
print(data[0])
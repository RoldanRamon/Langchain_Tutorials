# Import library
from langchain_community.document_loaders.csv_loader import CSVLoader

# Create a document loader for fifa_countries_audience.csv
loader = CSVLoader('./Material/fifa_countries_audience.csv')

# Load the document
data = loader.load()
print(data[0])
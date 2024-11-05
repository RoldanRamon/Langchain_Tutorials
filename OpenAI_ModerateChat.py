
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
# Busca a chave da API no arquivo .env
api_token = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_token)

# Create a request to the Moderation endpoint
response = client.moderations.create(
model="text-moderation-latest",
input="My favorite book is To Kill a Mockingbird.")

# Print the category scores
print(response.results[0].category_scores)
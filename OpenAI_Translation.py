from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
# Busca a chave da API no arquivo .env
api_token = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_token)

# Open the audio.m4a file
audio_file = open('audio.mp3', "rb")

# Create a translation from the audio file
response = client.audio.translations.create(model='whisper-1', file=audio_file)

# Extract and print the translated text
print(response.text)
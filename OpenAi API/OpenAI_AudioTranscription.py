from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
# Busca a chave da API no arquivo .env
api_token = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_token)

# Open the openai-audio.mp3 file
audio_file = open('audio.mp3', 'rb')

# Create a transcript from the audio file
response = client.audio.transcriptions.create(model="whisper-1", file=audio_file)

# Extract and print the transcript text
print(response.text)
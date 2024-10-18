import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
print("Escreva sua pergunta")
Question = input()
chat_completion = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[
        {
            "role": "user",
            "content": Question
        }
    ]
)

print(chat_completion.choices[0].message.content)

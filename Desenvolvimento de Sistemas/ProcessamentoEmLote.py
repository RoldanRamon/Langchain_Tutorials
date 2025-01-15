from openai import OpenAI
import os
from dotenv import load_dotenv
from tenacity import retry, wait_random_exponential, stop_after_attempt

load_dotenv()
# Busca a chave da API no arquivo .env
api_token = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_token)


@retry(wait=wait_random_exponential(min=5,max=40), stop=stop_after_attempt(4))
def get_response(model, message):
    response = client.chat.completions.create(
      model=model,
      messages=[message]
    )
    return response.choices[0].message.content

measurements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Initialize message list correctly
message = []

# Append system message correctly
message.append({
    "role": "system",
    "content": "Convert each measurement, given in kilometers, into miles, and reply with a table of all measurements. Também adicione uma coluna com a quantidade de anos de cachorro que equivalem esses km"
})

# Append user messages with proper string formatting
for m in measurements:
    message.append({
        "role": "user",
        "content": f"{m}"
    })

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=message
)

print(response.choices[0].message.content)

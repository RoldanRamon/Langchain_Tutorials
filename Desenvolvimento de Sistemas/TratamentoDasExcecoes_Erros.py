from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
# Busca a chave da API no arquivo .env
api_token = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_token)

message = {
    "role": "user",
    "content": "What is the capital of Brazil?"
}

# Use the try statement
try: 
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[message]
    )
    # Print the response
    print(response.choices[0].message.content)
# Use the except statement
except openai.AuthenticationError as e:
    print(f"OpenAI API failed to authenticate: {e}")
    pass
except openai.RateLimitError as e:
    print(f"OpenAI API request exceeded rate limit: {e}")
    pass   
except Exception as e:
    print(f"Unable to generate a response. Exception: {e}")
    pass 

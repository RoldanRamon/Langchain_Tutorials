from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

# Busca a chave da API no arquivo .env
api_token = os.getenv("OPENAI_API_KEY")

# Define the function definition
messages = [{'role': 'system',
  'content': "Don't make assumptions about what values to plug into functions. Ask for clarification if a user request is ambiguous. The sentiment should be positive or negative or neutral."},
 {'role': 'user',
  'content': "\nI recently purchased the steel color version of the thermal mug and I am absolutely thrilled with it! The mug keeps my drinks hot for hours, which is perfect for my long commutes. The steel color gives it a sleek and professional look that I love. Overall, I'm very happy with my purchase and would highly recommend this product to anyone in need of a reliable and stylish thermal mug.\n                 "}]

# Define the function definition
function_definition = [{'type': 'function',
  'function': {'name': 'extract_review_info',
   'description': 'Get the information about products and customer sentiment from the body of the input text',
   'parameters': {'type': 'object',
    'properties': {'product name': {'type': 'string',
      'description': 'Home type'},
     'product variant': {'type': 'string', 'description': 'Location'},
     'sentiment': {'type': 'string', 'description': 'Price'}}}}}]

# Create the OpenAI client
client = OpenAI(api_key=api_token)

response= client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    # Add the function definition
    tools=function_definition,
    # Specify the function to be called for the response
    tool_choice={"type": "function", "function": {"name": "extract_review_info"}}
)

# Print the response
print(response.choices[0].message.tool_calls[0].function.arguments)

# Cria uma tabela com os dados do json
dadosTabela = response.choices[0].message.tool_calls[0].function.arguments

# Chama agente para criar uma tabela com os dados do json
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "crie uma tabela com os dados desse json"},
    {"role": "user", "content": dadosTabela}
  ]
)

# Print the response
print(response.choices[0].message.content)
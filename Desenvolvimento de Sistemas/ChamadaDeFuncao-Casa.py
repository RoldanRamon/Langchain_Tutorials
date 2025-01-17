from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

# Busca a chave da API no arquivo .env
api_token = os.getenv("OPENAI_API_KEY")

# Define the message listing
message_listing = [{'role': 'system',
  'content': "Don't make assumptions about what values to plug into functions. Ask for clarification if a user request is ambiguous."},
 {'role': 'user',
  'content': 'Step into this beautiful two-story, single-family home located in Springfield, USA, priced at $350,000. This charming property features 4 bedrooms, 2.5 bathrooms, a spacious living room with a cozy fireplace, a modern kitchen with stainless steel appliances, and a large backyard perfect for family gatherings. The master bedroom includes an en-suite bathroom and a walk-in closet. Enjoy the convenience of an attached two-car garage and a recently updated HVAC system. Located near top-rated schools, parks, and shopping centers, this home is ideal for families looking for comfort and convenience.'}]

# Add the function definition
function_definition = [{'type': 'function',
  'function': {'name': 'real_estate_info',
   'description': 'Get the information about homes for sale from the body of the input text',
   'parameters': {'type': 'object',
    'properties': {'home type': {'type': 'string', 'description': 'Home type'},
     'location': {'type': 'string', 'description': 'Location'},
     'price': {'type': 'integer', 'description': 'Price'},
     'bedrooms': {'type': 'integer', 'description': 'Number of bedrooms'}}}}}]

# Create the OpenAI client
client = OpenAI(api_key=api_token)

# Call the API
response= client.chat.completions.create(
    model="gpt-4o-mini",
    # Add the message
    messages = message_listing,
    # Add your function definition
    tools = function_definition
)

# Print the response
print(response.choices[0].message.tool_calls[0].function.arguments)
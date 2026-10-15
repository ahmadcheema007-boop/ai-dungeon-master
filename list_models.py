from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client()

# Ask Google which models this key use, and print each name 
for model in client.models.list():
    print(model.name)
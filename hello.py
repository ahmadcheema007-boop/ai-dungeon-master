# --- IMPORTS: tell Python which tools this file needs. 

# "genai" is Google's library for talking to Gemini.
# It is installed as "google-genai" but imported from the "google" package.
from google import genai

# load_dotenv reads your .env file. The package is installed as 
# "python-dotenv" but imported as "dotenv".
from dotenv import load_dotenv 

# --- SETUP: get ready to talk to the API

# Read .env and copy each line (like GEMINI_API_KEY=...) into the programs
# environment variables. This must run BEFORE the client si created 
load_dotenv() 

# Create the client: the object that holds your connection settings.
# It finds the GEMINI_API_KEY in the environmental by itself, so the key
# never appears in your code (and can never leak through a commit)
client = genai.Client()





# THE REQUEST: send one message and store the reply ---

# generate_content sends your text to the model over the internet.
# Whatever comes back is stored in the variable "response". 
response = client.models.generate_content(

    # flash model
    model="gemini-3.5-flash-lite",

    # What you are saying to the model. A plain string works for one message. 
    # Later, for history, this becomes a list of past messages. 
    contents = [

        {"role": "user", "parts": [{"text": "My name is Ahmad and I'm a wizard."}]},
        {"role": "model", "parts": [{"text": "Well met, Ahmad! What is your speciality?"}]},
        {"role": "user", "parts": [{"text": "What's my name and what an I?"}]},
    ],

    # role says who spoke> Gemini uses "user" for you and "model" for the AI. 
    # parts is a list because a message can contain several pieces
    # List order matters. It is a conversation in sequence, ending with the newest question.

)


print(response.text) 
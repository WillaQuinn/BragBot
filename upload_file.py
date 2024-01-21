import openai
from dotenv import load_dotenv
import os


load_dotenv()  # This loads the environment variables from .env

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

with open("/Users/wbarnett/Desktop/HelloSciCom/BragBot:BoringBot/BragBotCode/BragDoc.txt", "rb") as file:
    response = openai.File.create(file=file, purpose="assistants")

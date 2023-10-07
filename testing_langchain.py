import os
import openai
import requests
import nltk
import json

nltk.download('punkt')

# Setup environment variables.
from dotenv import load_dotenv
load_dotenv()
key = os.getenv("OPENAI_API_KEY")
openai.api_key = key

print(key)
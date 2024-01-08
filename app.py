from flask import Flask, request, jsonify
from flask_cors import CORS

from dotenv import load_dotenv
import os
import requests

load_dotenv()  # This loads the environment variables from .env

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Welcome to my Flask app!'

@app.route('/chat', methods=['POST'])

def chat():
    user_input = request.form.get('message')

    # Prepare the data for the OpenAI API
    data = {
        "prompt": user_input,
        "max_tokens": 150  # Adjust as needed
    }

    print(user_input)

    # Set up the headers with your API key
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }

    # Make the POST request to the OpenAI API
    response = requests.post("https://api.openai.com/v1/engines/davinci/completions", json=data, headers=headers)
    print(response.status_code, response.text)

    # Extract the text from the OpenAI response
    openai_response = response.json().get('choices')[0].get('text', 'No response')

    return jsonify({'response': openai_response})


if __name__ == '__main__':
    app.run(debug=True)

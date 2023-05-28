import openai
import os
from dotenv import load_dotenv

# Load OpenAI key from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_KEY")

# Inisialisasi riwayat percakapan
conversation_history = [
    {"role": "system", "content": "You are a helpful assistant."},
]

def chat_with_model(prompt):
    conversation_history.append({"role": "user", "content": prompt})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation_history
    )

    conversation_history.append({"role": "assistant", "content": response.choices[0].message['content']})
    return response.choices[0].message['content']

# Loop untuk percakapan berkelanjutan
while True:
    user_input = input("You: ")
    response = chat_with_model(user_input)
    print("Chatbot: ", response)


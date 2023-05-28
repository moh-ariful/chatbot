import openai
import os
from dotenv import load_dotenv

# Load OpenAI key from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_KEY")

# Mulai model obrolan dengan openai.chatcompletion.create ()
def chat_with_model(prompt):
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

# Loop untuk percakapan berkelanjutan
while True:
    user_input = input("You: ")
    response = chat_with_model(user_input)
    print("Chatbot: ", response)

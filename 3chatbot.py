from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import os

# Load OpenAI key dari .env
load_dotenv()
api_key = os.getenv("OPENAI_KEY")

# Initialize Language Learning Model (LLM) with api_key moved to model_kwargs
llm = OpenAI(model_kwargs={'api_key': api_key}, temperature=0)

# Inisialisai conversation chain dengan ConversationBufferMemory
conversation = ConversationChain(
    llm=llm,
    verbose=True,
    memory=ConversationBufferMemory()
)

# Loop untu conversation terus menerus
while True:
    user_input = input("Kau: ")
    response = conversation.predict(input=user_input)
    print("Chatbot: ", response)



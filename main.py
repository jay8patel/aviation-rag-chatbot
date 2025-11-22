import os
from src.chat_core import get_agent_executor
from src.utils import validate_api_keys
from dotenv import load_dotenv

# Load env vars
load_dotenv()

def main():
    validate_api_keys()
    
    print("✈️  Aviation RAG Chatbot Initialized")
    print("Type 'exit' to quit.\n")
    
    agent_executor = get_agent_executor()

    while True:
        user_input = input("User: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        
        try:
            response = agent_executor.invoke({"input": user_input})
            print(f"Bot: {response['output']}\n")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
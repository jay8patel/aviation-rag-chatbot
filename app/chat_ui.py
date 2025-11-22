import streamlit as st
import sys
import os

# Add project root to path so imports work
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.chat_core import get_agent_executor
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Aviation RAG Chatbot", page_icon="✈️")

st.title("✈️ Aviation AI Assistant")
st.markdown("Ask about flight status, book tickets, or check airline policies.")

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize Agent (Singleton pattern for session)
if "agent" not in st.session_state:
    st.session_state.agent = get_agent_executor()

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input
if prompt := st.chat_input("How can I help you fly today?"):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Consulting flight systems..."):
            try:
                response_payload = st.session_state.agent.invoke({"input": prompt})
                response_text = response_payload["output"]
                st.markdown(response_text)
                st.session_state.messages.append({"role": "assistant", "content": response_text})
            except Exception as e:
                st.error(f"An error occurred: {e}")
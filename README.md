# Aviation RAG Chatbot ✈️

A full-stack AI application capable of tracking flights, booking tickets, and answering aviation policy questions using Retrieval Augmented Generation (RAG).

This project utilizes **LangChain** for orchestration, simulated **Google Cloud Vertex AI** for vector search, and a realistic **Flight API**.

## ✨ Features

1.  **Hybrid Routing**: Intelligently switches between RAG (for general questions) and API Tools (for real-time data).
2.  **RAG Pipeline**: Ingests aviation manuals (Baggage, Pets, Check-in rules) into a vector store for policy lookup.
3.  **Flight Tools**:
    *   `search_flights(origin, destination)`
    *   `check_flight_status(flight_id)`
    *   `book_flight(flight_id, name)`
4.  **GCP Ready**: Designed to interact with Google Cloud services, using a simulation layer for easy local testing.
5.  **Interactive UI**: Includes both a CLI tool and a Streamlit-based web interface.

## 🚀 Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/jay8patel/aviation-rag-chatbot.git
    cd aviation-rag-chatbot
    ```

2.  **Create a virtual environment**:
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # Mac/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up Environment**:
    You will need an OpenAI API key. Set it in your terminal or a `.env` file.
    ```bash
    # Windows PowerShell
    $env:OPENAI_API_KEY="sk-your-key-here"

    # Mac/Linux
    export OPENAI_API_KEY="sk-your-key-here"
    ```

## 🏃‍♂️ Usage

### Option 1: CLI Chatbot (Quickest Test)
Run the bot directly in your terminal:
```bash
python main.py
```
### Option 2: Chatbot in Web Interface
Launch the graphical interface using Streamlit:
```bash
streamlit run app/chat_ui.py
```

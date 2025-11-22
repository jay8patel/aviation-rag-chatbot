from langchain_openai import ChatOpenAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool

from src.flight_api import FlightAPI
from src.rag_pipeline import RAGPipeline

# Initialize Services
flight_api = FlightAPI()
rag_pipeline = RAGPipeline()

# --- Define Tools ---

@tool
def lookup_policy(query: str):
    """Search the aviation knowledge base for policies on baggage, pets, check-in, and refunds."""
    retriever_func = rag_pipeline.get_retriever_tool()
    return retriever_func(query)

@tool
def search_flights(origin: str, destination: str):
    """Search for available flights between two cities (e.g., JFK to LHR)."""
    return flight_api.search_flights(origin, destination)

@tool
def check_flight_status(flight_id: str):
    """Check the real-time status (delayed, on time) of a specific flight ID (e.g., UA101)."""
    return flight_api.get_flight_status(flight_id)

@tool
def book_flight_ticket(flight_id: str, passenger_name: str):
    """Book a flight given a flight ID and passenger name. Returns a PNR."""
    return flight_api.book_flight(flight_id, passenger_name)

tools = [lookup_policy, search_flights, check_flight_status, book_flight_ticket]

# --- Agent Setup ---

def get_agent_executor():
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an intelligent Aviation Assistant. "
                   "You verify flight statuses, book tickets, and answer policy questions. "
                   "Use 'lookup_policy' for general rules (bags, pets). "
                   "Use 'search_flights' or 'book_flight_ticket' for specific operations. "
                   "If you book a flight, always give the user their PNR."),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ])

    agent = create_tool_calling_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    return agent_executor
from src.gcp_vectorstore import GCPVectorStoreConnector

# Mock Knowledge Base Content (Simulating a PDF load)
AVIATION_KNOWLEDGE = [
    "Baggage Allowance: Economy passengers are allowed 1 carry-on bag (up to 10kg) and 1 checked bag (up to 23kg). Business class gets 2 checked bags.",
    "Check-in Policy: Online check-in opens 24 hours before departure and closes 60 minutes before takeoff. Airport counters close 45 minutes before departure.",
    "Prohibited Items: Explosives, compressed gases, flammable liquids, and sharp objects larger than 6cm are strictly prohibited in carry-on luggage.",
    "Pet Policy: Small pets (cats and dogs) can travel in the cabin if the carrier fits under the seat. Large pets must travel in the cargo hold.",
    "Refund Policy: Tickets are refundable within 24 hours of booking. Afterwards, standard cancellation fees apply based on fare class."
]

class RAGPipeline:
    def __init__(self):
        self.connector = GCPVectorStoreConnector()
        # Ingest data on initialization
        self.connector.ingest_documents(AVIATION_KNOWLEDGE)

    def get_retriever_tool(self):
        """
        Returns the retriever functionality specifically formatted for the Agent.
        """
        retriever = self.connector.get_retriever()
        
        def retrieve_aviation_policy(query: str):
            """Useful for answering general questions about airline rules, baggage, check-in, pets, and safety policies."""
            docs = retriever.invoke(query)
            return "\n\n".join([doc.page_content for doc in docs])
        
        return retrieve_aviation_policy
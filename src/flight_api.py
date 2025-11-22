import random
import string
import json
from datetime import datetime, timedelta

class FlightAPI:
    """
    A realistic mock API for flight operations.
    """

    def __init__(self):
        # Mock Database of Flights
        self.flights = [
            {"flight_id": "UA101", "origin": "JFK", "destination": "LHR", "status": "On Time", "price": 750, "dep_time": "18:00"},
            {"flight_id": "BA249", "origin": "LHR", "destination": "JFK", "status": "Delayed", "price": 820, "dep_time": "10:00"},
            {"flight_id": "DL505", "origin": "LAX", "destination": "HND", "status": "On Time", "price": 1200, "dep_time": "13:30"},
            {"flight_id": "AA990", "origin": "MIA", "destination": "GRU", "status": "Cancelled", "price": 600, "dep_time": "21:15"},
        ]

    def search_flights(self, origin: str, destination: str):
        """
        Search for flights between two airport codes.
        """
        origin = origin.upper()
        destination = destination.upper()
        results = [f for f in self.flights if f["origin"] == origin and f["destination"] == destination]
        
        if not results:
            return json.dumps({"message": f"No flights found from {origin} to {destination}."})
        return json.dumps(results)

    def get_flight_status(self, flight_id: str):
        """
        Check real-time status of a specific flight ID.
        """
        flight_id = flight_id.upper()
        for f in self.flights:
            if f["flight_id"] == flight_id:
                return json.dumps({
                    "flight_id": f["flight_id"],
                    "status": f["status"],
                    "departure": f["dep_time"]
                })
        return json.dumps({"error": "Flight ID not found."})

    def book_flight(self, flight_id: str, passenger_name: str):
        """
        Book a flight and generate a PNR.
        """
        flight_id = flight_id.upper()
        
        # Check if flight exists
        flight = next((f for f in self.flights if f["flight_id"] == flight_id), None)
        
        if not flight:
            return json.dumps({"error": "Cannot book. Flight ID not found."})
        
        if flight["status"] == "Cancelled":
            return json.dumps({"error": "Cannot book. Flight is cancelled."})

        # Generate Mock PNR
        pnr = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        
        booking_details = {
            "status": "confirmed",
            "pnr": pnr,
            "flight_id": flight_id,
            "passenger": passenger_name,
            "price": flight["price"]
        }
        return json.dumps(booking_details)
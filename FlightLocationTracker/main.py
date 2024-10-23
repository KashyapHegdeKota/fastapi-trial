import requests
import os
from dotenv import load_dotenv

load_dotenv()

access_key = os.getenv('ACCESS_KEY')

if access_key is None:
    print("API key not found in environment variables!")
else:
    params = {
        'access_key': access_key,
        'airline_iata': 'EK'  
    }

    api_result = requests.get('https://api.aviationstack.com/v1/flights', params)

    api_response = api_result.json()

    for flight in api_response['data']:
        print("Flight Date: ", flight.get('flight_date', 'N/A'))
        print("Flight Status: ", flight.get('flight_status', 'N/A'))
        
        departure = flight.get('departure', {})
        print("Departure Airport: ", departure.get('airport', 'N/A'))
        print("Departure IATA: ", departure.get('iata', 'N/A'))
        print("Scheduled Departure: ", departure.get('scheduled', 'N/A'))
        print("Actual Departure: ", departure.get('actual', 'N/A'))
        print("Departure Delay: ", departure.get('delay', 'N/A'))

        arrival = flight.get('arrival', {})
        print("Arrival Airport: ", arrival.get('airport', 'N/A'))
        print("Arrival IATA: ", arrival.get('iata', 'N/A'))
        print("Scheduled Arrival: ", arrival.get('scheduled', 'N/A'))
        print("Actual Arrival: ", arrival.get('actual', 'N/A'))
        print("Arrival Delay: ", arrival.get('delay', 'N/A'))

        airline = flight.get('airline', {})
        print("Airline: ", airline.get('name', 'N/A'))
        print("Flight Number: ", flight.get('flight', {}).get('number', 'N/A'))

        aircraft = flight.get('aircraft')
        if aircraft:
            print("Aircraft Registration: ", aircraft.get('registration', 'N/A'))
            print("Aircraft Model (IATA): ", aircraft.get('iata', 'N/A'))
        else:
            print("Aircraft Registration: N/A")
            print("Aircraft Model (IATA): N/A")

        live = flight.get('live', {})
        if live:
            print("Live Flight Data: ")
            print("  Latitude: ", live.get('latitude', 'N/A'))
            print("  Longitude: ", live.get('longitude', 'N/A'))
            print("  Altitude: ", live.get('altitude', 'N/A'))
            print("  Speed Horizontal: ", live.get('speed_horizontal', 'N/A'))
            print("  Speed Vertical: ", live.get('speed_vertical', 'N/A'))
            print("  Is Grounded: ", live.get('is_ground', 'N/A'))
        print("-" * 50)  

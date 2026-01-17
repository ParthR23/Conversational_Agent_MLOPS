import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class WeatherAgent:
    def __init__(self):
        self.api_key = os.getenv("WEATHER_API_KEY")
        if not self.api_key:
            raise ValueError("WEATHER_API_KEY not found in .env file")

    def run(self, query: str) -> str:
        city = query.split()[-1]

        response = requests.get(
            "https://api.weatherapi.com/v1/current.json",
            params={
                "key": self.api_key,
                "q": city
            }
        )

        response.raise_for_status()
        data = response.json()

        return f"The temperature in {city} is {data['current']['temp_c']}°C"

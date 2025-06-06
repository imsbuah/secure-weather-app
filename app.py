import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    if not city.isalpha():
        return "Invalid city name."
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code != 200:
        return "Error fetching weather data."
    data = response.json()
    return f"{data['name']}: {data['main']['temp']}°C, {data['weather'][0]['description']}"

if __name__ == "__main__":
    city = input("Enter city name: ")
    print(get_weather(city))

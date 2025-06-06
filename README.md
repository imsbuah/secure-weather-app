# Secure Weather App 🌤️🔐

A simple Python app that fetches weather data securely using the OpenWeather API.

## Features
- Input validation to prevent code injection
- API key security using `.env` file
- Uses `requests` and `dotenv` libraries

## Run Instructions
1. Install dependencies:
```
pip install -r requirements.txt
```

2. Create a `.env` file and add:
```
OPENWEATHER_API_KEY=your_api_key_here
```

3. Run the app:
```
python app.py
```

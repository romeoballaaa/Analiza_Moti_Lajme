import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_weather_data(city="Tirana"):
    api_key = os.getenv("WEATHER_API_KEY")
    # Shtojmë &units=metric që temperatura të jetë në Celsius
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            temp = data['main']['temp']
            desc = data['weather'][0]['description']
            return f"{temp}°C, {desc}"
        else:
            return "Informacioni i motit nuk u gjet"
    except Exception as e:
        return f"Gabim: {e}"
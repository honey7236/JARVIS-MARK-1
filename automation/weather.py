import requests

API_KEY = ""

def get_city_from_ip():
    try:
        res = requests.get("https://ipinfo.io/json")
        data = res.json()
        city = data.get("city")
        return city
    except Exception as e:
        print("Location Error:", e)
        return None


def get_weather():
    try:
        city = get_city_from_ip()

        if not city:
            return "Unable to detect your location"

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            return "Weather data not found"

        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        weather = data["weather"][0]["description"]

        return f"Current weather in {city}: {temp}°C, feels like {feels_like}°C with {weather}"

    except Exception as e:
        print("Weather Error:", e)
        return "Unable to fetch weather"
    
def display_weather():
    try:
        city = get_city_from_ip()

        if not city:
            return "Unable to detect your location"

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            return "Weather data not found"

        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        weather = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        return {
            "city": city,
            "temp": f"{temp}°C",
            "feels_like": f"{feels_like}°C",
            "description": weather.title(),
            "humidity": f"{humidity}%",
            "wind": f"{wind_speed} m/s"
        }

    except Exception as e:
        print("Weather Error:", e)
        return "Unable to fetch weather"
# x = get_weather()
# print(x)
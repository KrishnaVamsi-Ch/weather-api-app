import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city_name, "appid": api_key, "units": "metric"}

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            weather = data['weather'][0]['description'].capitalize()
            temperature = data['main']['temp']
            feels_like = data['main']['feels_like']
            print(f"🌤 Weather in {city_name}: {weather}")
            print(f"🌡 Temperature: {temperature}°C (Feels like {feels_like}°C)")
        else:
            print("❌ City not found or invalid API key.")

    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    city = input("Enter city name: ")
    api_key = input("Enter your OpenWeatherMap API key: ")
    get_weather(city, api_key)

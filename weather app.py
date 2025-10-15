import requests

def get_weather(location, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    if "main" in data:
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        desc = data["weather"][0]["description"]
        print(f"\nWeather for {location}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Conditions: {desc}")
    else:
        print(f"\nCould not find weather data for '{location}'. Please check the location and try again.")

if __name__ == "__main__":
    print("=== Python Weather App ===")
    api_key = input("Enter your OpenWeatherMap API key: ").strip()
    location = input("Enter city name: ").strip()
    get_weather(location, api_key)
import requests

print("Command-Line Weather App")

api_key = '5a2ac473377c1e6e3cf66433d672c980'
base_url = 'http://api.openweathermap.org/data/2.5/weather'

location = input("Enter city or ZIP code: ")

params = {
    'q': location,
    'appid': api_key,
    'units': 'metric'  # Use 'imperial' for Fahrenheit
}

response = requests.get(base_url, params=params)

if response.status_code == 200:
    weather_data = response.json()

    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    description = weather_data['weather'][0]['description']

    print("\nCurrent Weather:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Conditions: {description.capitalize()}")
else:
    print(f"Error fetching weather data. Status code: {response.status_code}")

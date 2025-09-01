import requests

API_KEY = 'your-api-key'
CITY = 'London'
URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}'

response = requests.get(URL)
data = response.json()

if response.status_code == 200:
    weather = data['weather'][0]['description']
    temperature = data['main']['temp'] - 273.15  # Convert Kelvin to Celsius
    print(f"Weather: {weather}")
    print(f"Temperature: {temperature:.2f}°C")
else:
    print("Error fetching data.")


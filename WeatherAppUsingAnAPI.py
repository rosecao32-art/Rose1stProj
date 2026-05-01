import requests

API_KEY = "06ceda1f2839a398abe656a6774506dc"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city: ")
params = {"q": city, "appid": API_KEY, "units": "metric"}

response = requests.get(BASE_URL, params=params)
data = response.json()

if response.status_code == 200:
    print(f"\nWeather in {data['name']}:")
    print("Temperature:", data['main']['temp'], "\N{DEGREE SIGN}C, which is", (data['main']['temp'] * 1.8) + 32, "\N{DEGREE SIGN}F" )
    print("Condition:", data['weather'][0]['description'].title())
    print("Humidity:", data['main']['humidity'], "%")
else:
    print("City not found. Please try again.")
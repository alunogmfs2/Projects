import requests

api_key = '2963dce9348037b72c1d3372e153adb9'
api_url = f'https://api.openweathermap.org/data/2.5/weather'

responce = requests.get(
    url=api_url,
    params={
        'q': 'Heidenheim',
        'appid': api_key,
        'units':'metric'  # Convert temperature to Celsius
    }
)

weather_data = responce.json()

print(weather_data)

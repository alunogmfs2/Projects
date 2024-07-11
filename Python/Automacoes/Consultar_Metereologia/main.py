import requests
import pywhatkit # type: ignore
import pyautogui


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

temperatura = weather_data['main']['temp']
temperatura_minima = weather_data['main']['temp_min']
temperatura_maxima = weather_data['main']['temp_max']
humidade = weather_data['main']['humidity']

print(f'Temperatura: {temperatura}°C')
print(f'Temperatura mínima: {temperatura_minima}°C')
print(f'Temperatura máxima: {temperatura_maxima}°C')
print(f'Humidade: {humidade}%')

pywhatkit.sendwhatmsg('+491772251975', f'Temperatura: {temperatura}°C, Temperatura mínima: {temperatura_minima}°C, Temperatura máxima: {temperatura_maxima}°C, Humidade: {humidade}%', 20, 10)
pyautogui.hotkey('winleft', '2')
pyautogui.sleep(0.1)
pyautogui.press('enter')

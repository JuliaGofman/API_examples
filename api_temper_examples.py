''' API-key ee49aeee22cae34422a9770aa994fa77
Используя API сайта OpenWeatherMap получить данные о погодных условиях в разных городах.
Считать из стандартной строки ввода название города и вывести для этого города температуру,
давление и влажность.
'''
import requests

api_url = "http://api.openweathermap.org/data/2.5/weather"
city = input("Input city: ")

params = {
    'q': city,
    'appid': 'ee49aeee22cae34422a9770aa994fa77',
    'units': 'metric'
}

res = requests.get(api_url, params=params)
# print(res.status_code)
# print(res.headers['Content-Type'])
# print(res.json())  or equal return json.loads(res.text)

data = res.json()
template = "Current temperature in {} is {}\u2103"
pressure = "Current pressure is {} hPa"
humidity = "Current humidity is {}\u0025"
print(template.format(city, data["main"]["temp"]))
print(pressure.format(data["main"]["pressure"]))
print(humidity.format(data["main"]["humidity"]))
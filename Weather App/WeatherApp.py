#_____Imports_____#
import requests
import json

#_____Global Variables_____#
city_name = input("Please enter the name of a city: ")
units = "Imperial"
API_key = "86d3e2dfd2e0b09cd53abeabe75eeadd"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units={units}&appid={API_key}"
response = requests.get(url)
data = response.json()

if response.status_code == 200:
    data = response.json()
    print('You Have Successfully Created A Post From The "Open Weather" API!')
    #print(json.dumps(data, indent=2))
    print(data['name'].title() + ' Weather Forecast')
    print('- Current Temperature: ' + str(round(data['main']['temp'])) + '°F')
    print('- Feels Like: ' + str(round(data['main']['feels_like'])) + '°F')
    print('- Min Temperature: ' + str(round(data['main']['temp_min'])) + '°F')
    print('- Max Temperature: ' + str(round(data['main']['temp_max'])) + '°F')
    print('- Humidity: ' + str(round(data['main']['humidity'])) + '%')
    print('- Wind Speed: ' + str(round(data['wind']['speed'])) + ' knots')
    print('- Condition: ' + (data['weather'][0]['description'].title()))
else:
    print(f'Error Creating Post: {response.status_code}')
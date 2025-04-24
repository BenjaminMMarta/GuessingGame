#_____Imports_____#
from flask import Flask
import requests
import json

# Create the Flask app
app = Flask(__name__)

# Define your routes
@app.route("/")
def home():
    return "<h1>Welcome to My Flask App!</h1>"

@app.route("/weather")
def getWeather():
    city_name = "London" #input("Please enter the name of a city: ")
    units = "Imperial"
    API_key = "86d3e2dfd2e0b09cd53abeabe75eeadd"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units={units}&appid={API_key}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        data = response.json()
    #print('You Have Successfully Created A Post From The "Open Weather" API!')
    #(json.dumps(data, indent=2))
        return f"""
        <p>Current Forecast For {city_name}:</p>
    <ul>
        <li>{'Current Temperature: ' + str(round(data['main']['temp'])) + '°F'}</li>
        <li>{'Feels Like: ' + str(round(data['main']['feels_like'])) + '°F'}</li>
        <li>{'Min Temperature: ' + str(round(data['main']['temp_min'])) + '°F'}</li>
        <li>{'Max Temperature: ' + str(round(data['main']['temp_max'])) + '°F'}</li>
        <li>{'Humidity: ' + str(round(data['main']['humidity'])) + '%'}</li>
        <li>{'Wind Speed: ' + str(round(data['wind']['speed'])) + ' knots'}</li>
        <li>{'Condition: ' + (data['weather'][0]['description'].title())}</li>
    </ul>
    """

# Start the Flask app
if __name__ == "__main__":
    app.run(port=8080, debug=True)
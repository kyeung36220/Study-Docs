from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/weather", methods=["POST"])
def get_weather():
    city = request.form["city"]
    return fetch_weather_by_city(city)

@app.route("/weather/location", methods=["POST"])
def get_weather_by_location():
    data = request.json
    latitude = data.get("latitude")
    longitude = data.get("longitude")

    # Fetch 7-day weather forecast with hourly data
    weather_data = fetch_weather_by_coordinates(latitude, longitude)
    if weather_data:
        return jsonify(weather_data)  # Send as JSON response for API call
    else:
        return "Could not fetch weather data.", 500

def fetch_weather_by_city(city):
    geocoding_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    geocoding_response = requests.get(geocoding_url).json()

    if "results" in geocoding_response and geocoding_response["results"]:
        location = geocoding_response["results"][0]
        latitude = location["latitude"]
        longitude = location["longitude"]
        city_name = location["name"]

        return fetch_weather_by_coordinates(latitude, longitude, city_name)
    else:
        return render_template("error.html", message="City not found!")

def convert_to_12hr_format(hour):
    hour_12 = hour % 12  # Convert hour to 12-hour format (0-11)
    period = 'AM' if hour < 12 else 'PM'
    if hour_12 == 0:  # Handle midnight hour (0:00 should be 12:00 AM)
        hour_12 = 12
    return f'{hour_12:02d}:00 {period}'


def fetch_weather_by_coordinates(latitude, longitude, city_name=None):
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_max,temperature_2m_min,weathercode&hourly=temperature_2m,weathercode&timezone=auto"
    weather_response = requests.get(weather_url).json()

    current_weather = weather_response.get("current_weather", {})
    daily_weather = weather_response.get("daily", {})
    hourly_weather = weather_response.get("hourly", {})

    daily_dates = [
        datetime.strptime(date, "%Y-%m-%d").strftime("%B %d")
        for date in daily_weather["time"]
    ]

    # Mapping Open-Meteo weather codes to icons
    weather_icon_mapping = {
        0: 'sunny.png',
        1: 'cloudy.png',
        2: 'cloudy.png',
        3: 'cloudy.png',
        45: 'fog.png',
        48: 'fog.png',
        51: 'rain.png',
        53: 'rain.png',
        55: 'rain.png',
        56: 'freezing_rain.png',
        57: 'freezing_rain.png',
        61: 'rain.png',
        63: 'rain.png',
        65: 'rain.png',
        66: 'freezing_rain.png',
        67: 'freezing_rain.png',
        71: 'snow.png',
        73: 'snow.png',
        75: 'snow.png',
        77: 'snow.png',
        80: 'rain.png',
        81: 'rain.png',
        82: 'rain.png',
        85: 'snow.png',
        86: 'snow.png',
        95: 'thunderstorm.png',
        96: 'thunderstorm.png',
        99: 'thunderstorm.png'
    }

    # Get the weather icon for the current condition
    current_weather_code = current_weather.get("weathercode")
    current_icon = weather_icon_mapping.get(current_weather_code, 'default.png')  # Default icon if code not found

    # Get the weather codes for daily forecasts
    daily_icons = [weather_icon_mapping.get(code, 'default.png') for code in daily_weather.get("weathercode", [])]

    # Get hourly icons
    hourly_icons = [weather_icon_mapping.get(code, 'default.png') for code in hourly_weather.get("weathercode", [])]

    weather = {
    "city": city_name if city_name else "Your Location",
    "current_temperature": current_weather.get("temperature"),
    "current_wind_speed": current_weather.get("windspeed"),
    "current_icon": current_icon,
    "daily":
    [
        {
            "date": daily_dates[i],  # Use formatted date
            "min_temp": round(int(daily_weather["temperature_2m_min"][i]) * (9/5) + 32),
            "max_temp": round(int(daily_weather["temperature_2m_max"][i]) * (9/5) + 32),
            "icon": daily_icons[i],
        }
        for i in range(len(daily_weather.get("time", [])))
    ],
    "hourly":
    [
        {
            "hour": convert_to_12hr_format(i),
            "temperature": round(int(hourly_weather["temperature_2m"][i]) * (9/5) + 32),
            "icon": hourly_icons[i]
        }
        for i in range(len(hourly_weather.get("temperature_2m", [])))
    ]
    }

    return render_template("result.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)

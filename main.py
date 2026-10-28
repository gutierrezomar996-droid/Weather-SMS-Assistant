import requests

def get_weather():
    base_url = "https://api.open-meteo.com/v1/forecast"

    params = {
    "latitude": 42.27113,
    "longitude": -89.094,
    "current": "temperature_2m,weather_code",
    "daily": "temperature_2m_max,temperature_2m_min",
    "temperature_unit": "fahrenheit",
    "timezone": "America/Chicago"
}

    response = requests.get(base_url, params=params,timeout=10)
    response.raise_for_status()  #handles api error

    weather_data = response.json()

    current_temperature = weather_data["current"]["temperature_2m"]
    weather_code = weather_data["current"]["weather_code"]
    daily_high = weather_data["daily"]["temperature_2m_max"][0]
    daily_low = weather_data["daily"]["temperature_2m_min"][0]

    return {
        "current_temp": current_temperature,
        "condition_code": weather_code,
        "daily_high": daily_high,
        "daily_low": daily_low
    }

weather = get_weather()
print(weather)
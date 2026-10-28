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

    #translation dictonary
    return {
        "current_temp": round(current_temperature),
        "condition_code": weather_code,
        "daily_high": round(daily_high),
        "daily_low": round(daily_low)
    }



def recommend_outfit(current_temp, condition_code):
    if current_temp < 30:
        outfit = "Very cold. Bring a heavy winter Jacket."
    elif  current_temp <= 49 :
        outfit =  "Mild  to cold weather throughout the day, Wear pants and a sweater."
    elif current_temp <= 59:
        outfit =  "Mild weather throughout the day, Wear pants and bring a sweater."
    elif current_temp <= 79:
        outfit =  "Warm weather throughout the day, Wear pants and a T-shirt."
    else:
        outfit =  "Hot weather throughout the day, Wear shorts and a T-shirt."


    if condition_code in [45,48]:
        outfit += "\nWeather Condition: Foggy. Be aware."
    elif condition_code in [51,53,55,56,57,61,63,65,66,67,80,81]:
        outfit+= "\nWeather Condition: Raining! Wear pants and Bring a sweater"
    elif condition_code in [71,73,75,85,86]:
        outfit += "\nWeather Condition: Snowing! Dress for snow."
    elif condition_code in [82,95,96,97,99]:
        outfit += "\nWeather Condition: Violent Weather! Dress appropriatly"
    
    return outfit


def build_message(weather):
    outfit = recommend_outfit(weather["current_temp"], weather["condition_code"])

    message = (
        f"Good Morning! its currently {weather["current_temp"]}°F right now.\n"
        f"Todays High will be {weather["daily_high"]}°F And Todays Low will be {weather["daily_low"]}°F.\n"
        f"{outfit}"
    )

    return message


weather = get_weather()

message = build_message(weather)
print(message)
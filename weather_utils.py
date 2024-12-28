import requests

# Function to fetch weather data
def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function for additional sentence ccording to weather condition 
def get_advice(weather):
    if 'rain' in weather['weather'][0]['description'].lower():
        return "Take an umbrella!"
    elif weather['main']['temp'] < 10:
        return "It's cold outside, wear a jacket!"
    elif weather['main']['temp'] > 30:
        return "It's hot, stay hydrated!"
    else:
        return "Looks like a pleasant day!"

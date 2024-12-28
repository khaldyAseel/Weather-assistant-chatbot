import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# Function to fetch weather data
def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function for friendly advice
def get_advice(weather):
    if 'rain' in weather['weather'][0]['description'].lower():
        return "Take an umbrella!"
    elif weather['main']['temp'] < 10:
        return "It's cold outside, wear a jacket!"
    elif weather['main']['temp'] > 30:
        return "It's hot, stay hydrated!"
    else:
        return "Looks like a pleasant day!"

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        city = request.form["Haifa"]
        api_key = "edc09ea9d70cc4e184b7362d4a728eaa"
        weather = get_weather(city, api_key)
        if weather:
            temp = weather['main']['temp']
            description = weather['weather'][0]['description']
            advice = get_advice(weather)
            return render_template("index.html", city=city, temp=temp, description=description, advice=advice)
        else:
            return render_template("index.html", error="City not found. Please try again.")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

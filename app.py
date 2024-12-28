from flask import Flask, render_template, request
from weather_utils import get_weather, get_advice

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    print("aseel")
    if request.method == "POST":
        city = request.form["city"] 
        print(f"City received: {city}")  
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


from flask import Flask, request, render_template
from API import weather


app = Flask(__name__)        
# daily_weather = [0, 0, 0, -1, -2, -1, 1, 1, 3, 5, 6, 6, 6, 9, 10, 10, 8, 7, 5, 3, 0, 0, -1, -2] # Celsium

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "GET":
        city = request.args.get("userCity")
        print(city)
    daily_weather = weather.get_weather(city=city)
    return render_template("weather.html",enumerate=enumerate, weather=daily_weather)
    


addr = "127.0.0.1"
app.run(host=addr,port=80,debug=True)
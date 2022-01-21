from flask import Flask, request, render_template, make_response
from flask.helpers import make_response
from werkzeug.wrappers import response
from API import weather


app = Flask(__name__)        
#daily_weather = [0, 0, 0, -1, -2, -1, 1, 1, 3, 5, 6, 6, 6, 9, 10, 10, 8, 7, 5, 3, 0, 0, -1, -2] # Celsium

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "GET":
        city = request.args.get("userCity")
        if not city:
            city = request.cookies.get("city")            
        print(city)
    daily_weather = weather.get_weather(city=city)
    if not city:
        response.set.cookie("city", city)
    response = make_response(render_template("weather.html",enumerate=enumerate, weather=daily_weather))
    response.set_cookie("city", city)
    return response
@app.route("/cookie")
def cookie():
    response = make_response("Coookie")    
    response.set_cookie("robotCookie", "This is one test of cookie", max_age = 60*60*24)
    return response
@app.route("/check_cookie")
def chek_cookie():
    if request.cookies.get("robotCookie"):
        response = make_response(f"Your cookie {request.cookies.get('robotCookie')}🍪")
    else:
        response = "0"
    return response




addr = "127.0.0.1"
app.run(host=addr,port=80,debug=True)
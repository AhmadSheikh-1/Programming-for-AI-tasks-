from flask import Flask, render_template
import requests 

app = Flask(__name__)

NASA_API = "Mgp1GB8jJ3TNqhCPIBHChCJJkGkof6qwcrcZQRBW"
APOD_URL = "https://api.nasa.gov/planetary/apod"

@app.route("/")
def index():
    params = {"api_key": NASA_API}
    response = requests.get(APOD_URL, params=params)
    apod_data = response.json()
    
    return render_template("index.html", apod=apod_data)

if __name__ == "__main__":
    app.run(debug=True)

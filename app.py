from flask import Flask, request, jsonify
app = Flask(__name__)
import requests

URL = f"https://randomuser.me/api/"

@app.route("/users")
def home():
    response = requests.get(URL)
    return response.json()

@app.route("/get-picture")
def getUserPic():
    response = requests.get(URL)
    getData = response.json()
    getResults = getData["results"]
    return getResults


if __name__ == "__main__":
    app.run(debug=True)
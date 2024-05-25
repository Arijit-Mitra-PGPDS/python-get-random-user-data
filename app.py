from flask import Flask, request, jsonify
app = Flask(__name__)
import requests

URL = f"https://randomuser.me/api/"

@app.route("/users")
def home():
    response = requests.get(URL)
    print(response)
    return response.json()


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask
import requests

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(error):
    return "<h1>404 Error</h1>", 404


@app.route("/google")
def get_google():
    response = requests.get("http://www.google.co.kr")
    return response.text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")

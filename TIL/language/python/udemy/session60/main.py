from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=['POST'])
def submit():
    return request.method, 200

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template
import requests

posts = requests.get("https://api.npoint.io/1efb8de1aa8190c154ac").json()
app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)

@app.route('/post')
def post():
    return render_template("post.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5001")
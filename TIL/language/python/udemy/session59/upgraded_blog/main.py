from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5001")
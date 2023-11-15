from flask import Flask, render_template, jsonify
import random
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    name = "SONG"
    random_number = random.randint(1,10)
    current_year = datetime.datetime.now().year
    
    return render_template("index.html", 
                           num = random_number,
                           year = current_year,
                           username = name)

@app.route('/guess/<name>')
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    
    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data["age"]
    
    return render_template("api.html",
                           username = name,
                           gender   = gender,
                           age      = age)
    
@app.route('/blog')
def blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = requests.get(blog_url)
    data = blog_response.json()
    
    return render_template("blog.html", posts = data)
    
if __name__ == "__main__":
    app.run(debug=True)
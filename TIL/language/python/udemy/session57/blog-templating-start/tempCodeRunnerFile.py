from flask import Flask, render_template
import requests, json

from post import Post

post_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(post_url)
all_posts = response.json()

print(json.dumps(all_posts, indent=4))
    
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", all_posts=all_posts)

@app.route('/post/<int:num>')
def show_post(num):
    return render_template('post.html', all_posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)
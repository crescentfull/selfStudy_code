from flask import Flask
from blog_view.test_blog_view import test_blog
import os

app = Flask(__name__)

print('main', os.path.dirname(os.path.realpath(__file__)) )
print (test_blog())
@app.route("/hello")
def test():                           
    return "Hello Flask!"

if __name__ == "__main__":              
    app.run(host="127.0.0.1", port="8080")
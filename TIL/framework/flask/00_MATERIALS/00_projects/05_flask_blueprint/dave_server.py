# dave_server.py
from flask import Flask
from sub_blueprint import blog_test

app = Flask(__name__)
app.register_blueprint(blog_test.blog_ab, url_prefix='/blog')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')

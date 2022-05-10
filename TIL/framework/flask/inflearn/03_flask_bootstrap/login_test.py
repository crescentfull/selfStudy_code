#프론트엔드와 백엔드 flask 로 한번에 구현해보기

import email
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

@app.route('/login')
def login():
    username = request.args.get('user_name')
    #파라미터 더 넣고 싶으면 더 넣으면 된다~
    password = request.args.get('pw')
    email    = request.args.get('email')
    print(username, password, email)
    print(type(username))
    print(type(password))
    print(type(email))
    if username == 'dave':
        return_data = {'auth' : 'success'}
    else:
        return_data = {'auth' : 'failed'}
    return jsonify(return_data)

@app.route('/html_test')
def hello_html():
    #html file은 templates 폴더에 위치해 있어야 한다.
    return render_template('login_rawtest.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080")
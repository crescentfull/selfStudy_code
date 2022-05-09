#프론트엔드와 백엔드 flask 로 한번에 구현해보기

from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/login')
def login():
    username = request.args.get('user_name')
    if username == 'dave':
        return_data = {'auth' : 'success'}
    else:
        return_data = {'auth' : 'failed'}
    return jsonify(return_data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080")
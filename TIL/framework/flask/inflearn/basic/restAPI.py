##
## REST API 구현
from flask import Flask, jsonify
app = Flask(__name__)

# data를 사전 데이터로 만들고, 이를 jsonify() 메서드에 넣어서 return 해주면 됨

@app.route('/json_test')
def hello_json():
    data = {'name' : '김대리', 'family' : 'Byun'}
    return jsonify(data)

@app.route('/server_info')
def server_json():
    data = { 'server_name' : '0.0.0.0', 'server_port' : '8080' }
    return jsonify(data)

if __name__ == "__main__":              
    app.run(host="0.0.0.0", port="8081")
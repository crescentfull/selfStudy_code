# 정적 페이지 리턴하기
from flask import Flask

app = Flask(__name__)

def add_file(data):
    return data + 5

@app.route("/")
def hello():                           
    return "<h1>Hello World!</h1>"

@app.route("/hello")
def hello_flask():
    return "<h1>Hello Flash!</h1>"

@app.route("/first")
def hello_first():
    return "<h3>Hello First</h3>"

@app.route("/profile/<username>") #<>로 파라미터 설정가능
def get_profile(username):
    return "profile: " + username

@app.route("/first/<username>")
def get_first(username):
    return "<h3>Hello first" + username + "!</h3>"

@app.route("/message/<int:message_id>") #파라미터에 데이터타입 설정 가능
def get_message(message_id):
    return "message id: %d" % message_id   # %d 는 int, %f 는 float, %s 는 string

@app.route("/message2/<int:messageid>")
def get_message2(messageid):
    data = add_file(messageid)
    return "<h1>%d</h1>" % (data)

if __name__ == "__main__":              
    app.run(host="127.0.0.1", port="8080")
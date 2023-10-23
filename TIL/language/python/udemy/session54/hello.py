'''
파이썬 백엔드 플라스크 장고 fast
플라스크 -> 초보개발, 소규모
장고 -> 대규모 서비스

백엔드란?
클라이언트, 서버, database

프레임워크 VS 라이브러리
라이브러리는 특정 작업시에 특정 라이브러리르 호출
프레임워크는 우리가 프레임워크 규칙에 맞게 아키텍처를 사용하여 특정 기능을 실행할 때 프레임워크가 그것에 맞는 코드를 실행한다.

환경변수로 flask 서버 run가능

>>> export FLASK_APP={메인파일} //환경변수추가
>>> flask run
'''

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
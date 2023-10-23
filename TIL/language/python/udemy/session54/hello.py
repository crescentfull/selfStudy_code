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
# __name__은 파이썬에 내장된 특수속성의 하나이다.
# __name__에 접근하면 현재 사용 중인 클래스나 함수, 메소드, 디스크립터의 이름을 알 수 있다.
# flask는 __name__을 받으면 현재 실행 중인 파일에 애플리케이션 코드가 있는지 확인한다.
# 

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run()

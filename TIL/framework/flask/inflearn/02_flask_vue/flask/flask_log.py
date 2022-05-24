# from flask import Flask
# import requests

# app = Flask(__name__)

# if not app.debug:
#     import logging
#     from logging.handlers import RotatingFileHandler  # logging 핸들러 이름을 적어줌
#     file_handler = RotatingFileHandler(
#         'dave_server.log', maxBytes=2000, backupCount=10)
#     file_handler.setLevel(logging.WARNING)  # 어느 단계까지 로깅을 할지를 적어줌
#     # app.logger.addHandler() 에 등록시켜줘야 app.logger 로 사용 가능
#     app.logger.addHandler(file_handler)


# @app.errorhandler(404)
# def page_not_found(error):
#     app.logger.error('이것은 중요한 에러입니다. page_not_found에서 일어났습니다.')
#     return "<h1>해당 경로에 맞는 웹페이지가 없습니다. 문제가 지속되면, 죄송하지만 관리자에게 연락해주세요</h1>", 404


# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port="8080", debug=False)

from flask import Flask 
import requests

app = Flask(__name__)

# 2021.12.06 업데이트
# 최근에는 app.debug 값을 app.run 에서 설정하기 전에, 미리 설정해주어야, 하단부 if not app.debug 에 설정이 
# 적용되는 것을 확인하였습니다. 따라서, app.debug 값을 미리 설정해주는 코드를 추가하였습니다
# 즉, app.run 에서의 debug 옵션과, app.debug 값을 기반으로 한 logging 설정은 분리된 설정으로 이해하시면 좋을 것 같습니다
app.debug = False

if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler # logging 핸들러 이름을 적어줌
    file_handler = RotatingFileHandler('dave_server.log', maxBytes=2000, backupCount=10) 
    file_handler.setLevel(logging.WARNING) # 어느 단계까지 로깅을 할지를 적어줌
    app.logger.addHandler(file_handler) # app.logger.addHandler() 에 등록시켜줘야 app.logger 로 사용 가능

@app.errorhandler(404)
def page_not_found(error):
    app.logger.error(error)
    return "<h1>404 Error</h1>", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")
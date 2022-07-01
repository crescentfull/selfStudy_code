
from flask import Flask, jsonify, request, render_template, make_response
from flask_login import LoginManager, login_manager, current_user, login_required, logout_user
from flask_cors import CORS #CORS 정책 

from blog_control.user_mgmt import User
from blog_view import blog

import os 
#보안 로그인할때 많이 사용하는 oauth2 ex;google,kakao 등 http 에서 테스트하기 위해서 사용

#https 만 지원하는 기능을 http에서 테스트할때 사용하는 변수
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__, static_url_path='/static')
CORS(app)
app.secret_key = 'song_server1' #보안 정책을 더 높일려면 서버를 킬때마다 갱신해주는 방법이 있다. 하지만 지금은 그렇게 해버리면 세션값들이 다 날아가기 때문에 고정값으로 하였다.

app.register_blueprint(blog.blog_abtest, url_prefix = '/blog')

login_manager = LoginManager()
login_manager.init_app(app) #login_manager에 flask app 등록
login_manager.session_protection = 'strong' # session을 보다 복잡하게 만든다

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id) #데이터베이스에서 데이터를 가져와서 객체로 리턴해줘야함

@login_manager.unauthorized_handler
def unauthorized():
    return make_response(jsonify(success = 'False'), 401) # 401 = 불허용

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)
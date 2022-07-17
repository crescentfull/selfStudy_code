from flask import Flask, Blueprint, request, render_template, make_response, jsonify, redirect, url_for, session
from flask_login import login_user, current_user, logout_user

from blog_control.user_mgmt import *
from blog_control.session_mgmt import *

import datetime

blog_abtest = Blueprint('blog', __name__)


@blog_abtest.route('/set_email', methods=['GET','POST'])
def set_email():
    if request.method == 'GET':
        #print('set_email : ', request.headers)
        print('set_email : ', request.args.get('user_email'))
        return redirect(url_for('blog.blog_fullstack')) # 1
    else:
        #print('set_email : ', request.headers)
        #print('set_email : ', request.get_jso n()) # content type이 application/json인 경우
        #print('set_email : ', request.form['user_email'])
        user = User.create(request.form['user_email'], request.form['blog_id'])
        login_user(user, remember=True, duration=datetime.timedelta(days=365))
        
        return redirect(url_for('blog.blog_fullstack'))
    # return redirect('/blog/test') # 2
    # 1,2번중 더 편하고 적합한 것으로 사용하면 된다.
    # return make_response(jsonify(SUCCESS=True), 200)

@blog_abtest.route('/logout')
def logout():
    User.delete(current_user.id)
    logout_user()
    return redirect(url_for('blog.test'))
    
@blog_abtest.route('/blog_fullstack')
def blog_fullstack():
    if current_user.is_authenticated:
        webPageName = BlogSession.get_blog_page(current_user.blog_id)
        return render_template(webPageName, user_email=current_user.user_email)
    else:
        webPageName = BlogSession.get_blog_page()
        BlogSession.save_session_info(session['client_id'],'anonymous', webPageName)
        return render_template(webPageName)
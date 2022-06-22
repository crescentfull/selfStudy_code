from db_model.mongoDB import conn_mongo
from datetime import datetime

class BlogSession():
    blog_page = {'A' : 'blog_A.html', 'B':'blog_B.html'}
    session_count = 0
    
    @staticmethod
    def save_session_info(session_ip, user_email, webpage_name):
        now = datetime.now()
        now_time = now.strftime("%d/%m/%Y %H:%M:%S") # https://strftime.org/
        
        mongo_db = conn_mongo()
        mongo_db.insert_one({
            'session_ip' : session_ip,
            'user_email' : user_email,
            'page'       : webpage_name,
            'access_time' : now_time
        })
    
    @staticmethod
    def get_blog_page(blog_id=None):
        if blog_id == None:
            if BlogSession.session_count == 0:
                BlogSession.session_count == 1:
                return 'blog_A.html'
            else:
        else:
            
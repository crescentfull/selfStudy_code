import pymongo
import config

MONGO_HOST = config.DB_CONFIG['host']
MONGO_CONN = pymongo.MongoClient('mongodb://%s' % (MONGO_HOST))

def conn_mongo():
    try:
        MONGO_CONN.admin.command(config.DB_CONFIG['user'])
        blog_ab = MONGO_CONN.blog_session_db.blog_ab
    except:
        MONGO_CONN = pymongo.MongoClient('mongodb://%s' % (MONGO_HOST))
        blog_ab = MONGO_CONN.blog_session_db.blog_ab
    return blog_ab
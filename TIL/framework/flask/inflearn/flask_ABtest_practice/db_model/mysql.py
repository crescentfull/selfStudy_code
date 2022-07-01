import pymysql
from db_model import config

MYSQL_HOST = config.DB_CONFIG['host']
MYSQL_CONN = pymysql.connect(
    host     = MYSQL_HOST,
    port     = config.DB_CONFIG['port'],
    user     = config.DB_CONFIG['user'],
    password = config.DB_CONFIG['password'],
    db       = config.DB_CONFIG['db'],
    charset  = 'utf8'
)

def conn_mysql():
    if not MYSQL_CONN.open:
        MYSQL_CONN.ping(reconnect=True)
    return MYSQL_CONN
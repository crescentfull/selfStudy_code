DATABASES = {
    'default' : {
        'ENGINE'    : 'django.db.backends.mysql',
        'NAME'      : 'test',
        'USER'      : 'root',
        'PASSWORD'  : '12341234',
        'HOST'      : '127.0.0.1',
        'PORT'      : '3306',
        'OPTIONS'   : {
                      'init_command' : "SET sql_mode='STRICT_TRANS_TABLES'",
                      }
    }
}

SECRET_KEY = 'django-insecure-y7d7$f28eu8wh)dj9lj!y6v+5t!-v+t3n$0plf0($0b)%+m3g6'
ALGORITHMS = 'HS256'
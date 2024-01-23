from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)

# MySQL 설정
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'yourusername'
app.config['MYSQL_DATABASE_PASSWORD'] = 'yourpassword'
app.config['MYSQL_DATABASE_DB'] = 'yourdatabase'

mysql = MySQL()
mysql.init_app(app)

@app.route('/')
def index():
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * FROM your_table")
    data = cursor.fetchall()
    return str(data)

if __name__ == "__main__":
    app.run(debug=True)
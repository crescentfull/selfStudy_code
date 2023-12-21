from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 데이터베이스 생성
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 데이터베이스 생성
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    print("all_books : ", all_books)
    return render_template("index.html", books=all_books)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # new_book = {
        #     "title" : request.form["title"],
        #     "author" : request.form["author"],
        #     "rating" : request.form["rating"]
        # }
        new_book = request.form.to_dict()
        all_books.append(new_book)
        print("new_book : ", new_book)
        return redirect(url_for('home'))
    
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)


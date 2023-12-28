# from flask import Flask, render_template, request, redirect, url_for
# from flask_sqlalchemy import SQLAlchemy
# from flask import current_app


# app = Flask(__name__)

# # 데이터베이스 생성
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# # 데이터베이스 생성
# class Book(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(250), unique=True, nullable=False)
#     author = db.Column(db.String(250), nullable=False)
#     rating = db.Column(db.Float, nullable=False)
    
# with app.app_context():
    
#     all_books = db.session.query(Book).all()
#     db.create_all()


# @app.route('/')
# def home():
    
#     print("all_books : ", all_books)
#     return render_template("index.html", books=all_books)

# @app.route("/add", methods=["GET", "POST"])
# def add():
#     if request.method == "POST":
#         new_book = {
#             "title" : request.form["title"],
#             "author" : request.form["author"],
#             "rating" : request.form["rating"]
#         }
#         # new_book = request.form.to_dict()
#         # all_books.append(new_book)
#         db.session.add_all(new_book)
#         db.session.commit()
#         print("new_book : ", new_book)
#         return redirect(url_for('home'))
    
#     return render_template("add.html")


# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)


@app.route('/', methods=['GET', 'POST'])
def home():
    with app.app_context():
        all_books = db.session.query(Books).all()
    return render_template('index.html', library=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "GET":
        return render_template('add.html')
    else:
        book = request.form['book']
        author = request.form['author']
        rating = request.form['rating']
        with app.app_context():
            db.create_all()
            new_book = Books(title=book, author=author, rating=rating)
            db.session.add(new_book)
            db.session.commit()
        return redirect('/')

@app.route("/edit", methods=['GET', 'POST'])
def edit():
    id = request.args.get('id')
    if request.method == 'GET':
        with app.app_context():
            book = db.session.query(Books).filter_by(id=id).first()
        return render_template('edit.html', book=book)
    else:
        new_rating = request.form['rate']
        with app.app_context():
            book_update = db.session.query(Books).filter_by(id=id).first()
            book_update.rating = new_rating
            db.session.commit()
        return redirect('/')

@app.route('/delete')
def delete():
    with app.app_context():
        id = request.args.get('id')
        book_to_delete = db.session.query(Books).filter_by(id=id).first()
        db.session.delete(book_to_delete)
        db.session.commit()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
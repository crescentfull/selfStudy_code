from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Flask 애플리케이션 인스턴스 생성
app = Flask(__name__)

##CREATE DATABASE
# 'SQLALCHEMY_DATABASE_URI'는 사용하는 데이터베이스에 맞게 설정
# 예: SQLite를 사용하는 경우 'sqlite:///example.db'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
#Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# SQLAlchemy 인스턴스 생성
db = SQLAlchemy(app)


##CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    
    # __repr__(self): 메서드는 Python에서 클래스의 인스턴스를 문자열로 표현하는 방법을 정의. 
    # 이 메서드는 클래스의 객체가 어떻게 출력될지를 결정하며, 주로 디버깅과 로깅 목적으로 사용
    def __repr__(self):
        return f'<Book {self.title}>'

# 애플리케이션 컨텍스트 내에서 데이터베이스 테이블 생성
# 이렇게 함으로써 Flask 애플리케이션 설정에 접근할 수 있음    
with app.app_context():
    db.create_all()
    # db.drop_all()

    ## 레코드생성
    # new_book = Book(title="Harry Potter", author="J.K.Rowling", rating="9.3")
    # db.session.add(new_book)
    # db.session.commit()
    
    ## 특정 레코드 조회
    book = Book.query.filter_by(title="Harry Potter").first()
    
    ## 모든 레코드 조회
    # all_books = db.session.query(Book).all()
    
    ## 특정 레코드 업데이트
    # book_to_update = Book.query.filter_by(title="Harry Potter").first()
    # book_to_update.title = "Harry Potter and the Chmber of Secrets"
    # db.session.commit()
    
    ## 기본키 레코드 업데이트
    # book_id = 1
    # book_to_update = Book.query.get(book_id)
    # book_to_update.title = "Harry Potter and the Goblet of fire"
    # db.session.commit()
    
    ## 기본키로 특정 레코드 삭제
    # book_id = 1
    # book_to_delete = Book.query.get(book_id)
    # db.session.delete(book_to_delete)
    # db.session.commit()
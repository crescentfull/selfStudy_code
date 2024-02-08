from flask import Flask, jsonify, render_template, request, current_app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
from dotenv import load_dotenv

import random
import os

app = Flask(__name__)

##Connect to Database
load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)
    
    def to_dict(self):
            """ 객체 속성을 딕셔너리로 변화 """
            return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    if cafes:
        random_cafe = random.choice(cafes)
        return jsonify(cafe=random_cafe.to_dict())
    else:
        return jsonify(error={"NOT FOUND":"No cafes found in the database."}), 404

@app.route("/all")
def get_all_cafes():
    cafes = db.session.query(Cafe).all()
    return jsonify(cafe=[cafe.to_dict() for cafe in cafes]) # list에 dict 

@app.route("/search")
def get_cafe_location():
    try:
        query_location = request.args.get("loc")
        query_name = request.args.get("name")

        if not query_location and not query_name:
            raise ValueError("At least one of 'loc' or 'name' parameters must be provided.")

        query_conditions = []
        if query_location:
            query_conditions.append(Cafe.location.like(f"%{query_location}%"))
        if query_name:
            query_conditions.append(Cafe.name.like(f"%{query_name}%"))

        cafes = db.session.query(Cafe).filter(or_(*query_conditions)).all()

        if cafes:
            return jsonify(cafe=[cafe.to_dict() for cafe in cafes])
        else:
            return jsonify(error={"NOT FOUND": "Sorry, we couldn't find a matching cafe"}), 404
    except ValueError as e:
        return jsonify(error={"Invalid Request": str(e)}), 400
    except Exception as e:
        return jsonify(error={"Unexpected Error": str(e)}), 500

# @app.route("/search/<name>")
# def get_cafe_name(name):
#     query_location = request.args.get(name)
#     cafes = db.session.query(Cafe).filter(Cafe.name.like(f"%{name}%")).all()
#     if cafes:
#         return jsonify(cafe=[cafe.to_dict() for cafe in cafes] )
#     else:
#         return jsonify(error={"NOT FOUND":"Sorry, we don't have a cafe as that name"}), 404
    
## HTTP POST - Create Record
@app.route("/add", methods=['POST'])
def add_new_cafe():
    try:
        data = request.get_json()
        new_cafe = Cafe(
                    name        = data['name'],
                    map_url     = data['map_url'],
                    img_url     = data['img_url'],
                    location    = data['location'],
                    seats       = data['seats'],
                    has_toilet  = data['has_toilet'],
                    has_wifi     = data['has_wifi'],
                    has_sockets = data['has_sockets'],
                    can_take_calls = data['calls'],
                    coffee_price = data['price']
        )
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify({"message": "User added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record

with app.app_context():
    db.create_all()
    
if __name__ == '__main__':
    app.run(debug=True)

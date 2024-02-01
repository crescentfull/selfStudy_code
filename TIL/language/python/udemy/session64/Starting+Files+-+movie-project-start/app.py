from flask import Flask, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap
from models import db, Movie
from forms import UpdateMovieForm, FindMovieForm
from config import Config
import requests

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    Bootstrap(app)
    db.init_app(app)
    
    MOVIE_DB_API_KEY = Config.MOVIE_DB_API_KEY
    MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"

    @app.route("/")
    def home():
        all_movies = Movie.query.all()
        return render_template("index.html", movie_list=all_movies)


    @app.route("/add", methods=["GET", "POST"])
    def add_movie():
        form = FindMovieForm()
        
        if form.validate_on_submit():
            movie_title = form.title.data
            response = requests.get(MOVIE_DB_SEARCH_URL, params={"api_key": MOVIE_DB_API_KEY, "query": movie_title})
            data = response.json()["results"]
            return render_template("select.html", options=data)
        return render_template("add.html", form=form)
    
    @app.route("/find")
    def find_movie():
        MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
        MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"
        movie_api_id = request.args.get("movie_id")
        
        if movie_api_id:
            movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
            response = requests.get(movie_api_url, params={"api_key": MOVIE_DB_API_KEY, "language": "en-US"})
            data = response.json()
            new_movie = Movie(
                title=data["original_title"],
                year=data["release_date"].split("-")[0],
                img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
                description=data["overview"],
                rating=data["vote_average"],
                review=data["title"]
            )
            db.session.add(new_movie)
            db.session.commit()
            return redirect(url_for("update", movie_id=new_movie.id))
    
    @app.route("/update", methods=["GET","POST"])
    def update():
        form = UpdateMovieForm()
        movie_id = request.args.get("movie_id") #
        movie = Movie.query.get(movie_id)
        
        if form.validate_on_submit():
            movie.rating = float(form.rating.data)
            movie.review = form.review.data
            db.session.commit()
            return redirect(url_for('home'))
        return render_template("edit.html", movie=movie, form=form)
    
    @app.route("/delete/<int:movie_id>")
    def delete(movie_id):
            post = Movie.query.get(movie_id)
            db.session.delete(post)
            db.session.commit()
            flash('삭제하였습니다.')
            return redirect(url_for('home'))
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
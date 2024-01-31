from flask import Flask, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap
from models import db, Movie
from forms import MovieForm, UpdateMovieForm, FindMovieForm
from config import Config

import requests

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    Bootstrap(app)
    db.init_app(app)

    @app.route("/")
    def home():
        all_movies = Movie.query.all()
        return render_template("index.html", movie_list=all_movies)


    @app.route("/add", methods=["GET", "POST"])
    def add_movie():
        form = FindMovieForm()
        if form.validate_on_submit():
            MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
            MOVIE_DB_API_KEY = Config.MOVIE_DB_API_KEY
            movie_title = form.title.data
            response = requests.get(MOVIE_DB_SEARCH_URL, params={"api_key": MOVIE_DB_API_KEY, "query": movie_title})
            data = response.json()["results"]
            return render_template("select.html", options=data)
        return render_template("add.html", form=form)
    # def add():
        # form = MovieForm()
        # if form.validate_on_submit():
        #     new_movie = Movie(
        #         title=form.title.data,
        #         year=form.year.data,
        #         description=form.description.data,
        #         rating=form.rating.data,
        #         ranking=form.ranking.data,
        #         review=form.review.data,
        #         img_url=form.img_url.data
        #     )
        #     db.session.add(new_movie)
        #     db.session.commit()
        #     return redirect(url_for('home'))
        #         # 데이터 추가 test
        # new_movie = Movie(
        #     title="Phone Booth",
        #     year=2002,
        #     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
        #     rating=7.3,
        #     ranking=10,
        #     review="My favourite character was the caller.",
        #     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
        # )
        # db.session.add(new_movie)
        # db.session.commit()
        # return redirect(url_for('home'))
        return render_template("add.html", form=form)
    
    @app.route("/update", methods=["GET","POST"])
    def update():
        form = UpdateMovieForm()
        movie_id = request.args.get("movie_id")
        print(movie_id)
        movie = Movie.query.get(movie_id)
        print(movie)
        print("form.rating.data : ", form.rating.data)
        print("form.review.data : ", form.review.data)
        if form.validate_on_submit():
            movie.rating = float(form.rating.data)
            movie.review = form.review.data
            db.session.commit()
            return redirect(url_for('home'))
        return render_template("edit.html", movie=movie, form=form)
    
    @app.route("/delete/<int:movie_id>")
    def delete(movie_id):
            post = Movie.query.get(movie_id)
            print(post)
            db.session.delete(post)
            db.session.commit()
            flash('삭제하였습니다.')
            return redirect(url_for('home'))
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
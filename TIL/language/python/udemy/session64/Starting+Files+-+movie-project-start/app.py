from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from models import db, Movie
from forms import MovieForm
from config import Config

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
    def add():
        form = MovieForm()
        if form.validate_on_submit():
            new_movie = Movie(
                title=form.title.data,
                year=form.year.data,
                description=form.description.data,
                rating=form.rating.data,
                ranking=form.ranking.data,
                review=form.review.data,
                img_url=form.img_url.data
            )
            db.session.add(new_movie)
            db.session.commit()
            return redirect(url_for('home'))
        return render_template("add.html", form=form)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
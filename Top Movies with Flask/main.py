from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests as r
from dotenv import load_dotenv
from os import getenv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# Create Movie Table
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movie.db"
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Movie(db.Model):
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    title : Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    year : Mapped[int] = mapped_column(Integer, nullable=False)
    description : Mapped[str] = mapped_column(String(500), nullable=False)
    rating : Mapped[float] = mapped_column(Float, nullable=True)
    ranking : Mapped[int] = mapped_column(Integer, nullable=True)
    review : Mapped[str] = mapped_column(String(250), nullable=True)
    img_url : Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()

# Create Edit Movie Form
class RateMovieForm(FlaskForm):
    rating = FloatField("Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")

class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")

load_dotenv()
TMDB_ACCESS_TOKEN = getenv("TMDB_ACCESS_TOKEN")
headers = {
    "accept" : "application/json",
    "Authorization" : f"Bearer {TMDB_ACCESS_TOKEN}"
}

@app.route("/")
def home():
    movies = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars().all()
    
    rank_number = 1
    for movie in reversed(movies):
        movie.ranking = rank_number
        rank_number += 1
    
    return render_template("index.html", movies=movies[::-1])

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    form = RateMovieForm()
    movie = db.get_or_404(Movie, id)
    if form.validate_on_submit():
        new_rating = float(request.form["rating"])
        new_review = request.form["review"]
        movie.rating = new_rating
        movie.review = new_review
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=form, movie=movie)

@app.route("/delete/<int:id>")
def delete(id):
    movie = db.get_or_404(Movie, id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=["GET", "POST"])
def add():
    form = FindMovieForm()
    if form.validate_on_submit():
        movie_title = request.form["title"]
        url = "https://api.themoviedb.org/3/search/movie?include_adult=false&language=en-US&page=1"
        response = r.get(url, headers=headers, params={"query": movie_title})
        response.raise_for_status()
        queried_movies = response.json()["results"]
        return render_template("select.html", movies=queried_movies)
    return render_template("add.html", form=form)

@app.route("/get_movie_details/<int:id>")
def get_movie_details(id):
    url = f"https://api.themoviedb.org/3/movie/{id}?language=en-US"
    response = r.get(url, headers=headers)
    response.raise_for_status()
    movie_data = response.json()
    
    new_movie = Movie(
        title = movie_data["original_title"],
        year = movie_data["release_date"][:4],
        description = movie_data["overview"],
        img_url = f"https://image.tmdb.org/t/p/w600_and_h900_face{movie_data['poster_path']}"
    )
    
    db.session.add(new_movie)
    db.session.commit()
    
    return redirect(url_for('edit', id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)

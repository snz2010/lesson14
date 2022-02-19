from flask import Flask, request, render_template
from utils import search_film, from_to, get_rating, get_genre

app = Flask(__name__)


@app.route('/')  # страница "МЕНЮ"
def page_index():
    return render_template("index.html")


# 1. Поиск по названию
@app.route("/movie/")
def page_movie():
    title = request.args.get("title")
    if title == "":
        return "<h2>Не введено название фильма</h2>"
    movie = search_film(title)
    return render_template('movie.html', film=movie)


# 2. Поиск по годам выпуска
@app.route("/between/")
def page_between():
    min_year = request.args.get("min_year")
    max_year = request.args.get("max_year")
    if min_year == "":
        return "<h2>Не введен год выпуска фильма (min)</h2>"
    if max_year == "":
        return "<h2>Не введен год выпуска фильма (max)</h2>"
    movies = from_to(min_year, max_year)
    return render_template('from_to.html', films=movies)


# 3. Поиск по рейтингу
@app.route("/rating/")
def page_rating():
    rating = request.args.get("rating")
    if rating == "":
        return "<h2>Не выбран рейтинг фильмов</h2>"
    movies = get_rating(rating)
    return render_template('rating.html', films=movies)


# 4. Поиск по жанру
@app.route("/genre/")
def page_genre():
    g = request.args.get("genre")
    if g == "":
        return "<h2>Не выбран жанр фильмов</h2>"
    movies = get_genre(g)
    return render_template('genre.html', films=movies)


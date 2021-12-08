from datetime import date

from dateutil.relativedelta import relativedelta

from app import app, tmdb
from flask import request, render_template, url_for

@app.route('/')
@app.route('/index')
def index():
    return 'HELLO WORLD!'
@app.route('/movies', methods=["GET", "POST"])
def movies():
    page = request.args.get("page", 1, type=int)

    year = request.args.get("year", date.today().year, type=int)
    month = request.args.get("month", date.today().month, type=int)

    movies = tmdb.monthly_movies(month, year, page)

    current_date = date(year, month, 1)

    next_month = current_date + relativedelta(months=+1)
    prev_month = current_date + relativedelta(months=-1)

    dates = {
        "month": month,
        "year": year,
        "next_month": next_month.month,
        "next_year": next_month.year,
        "prev_month": prev_month.month,
        "prev_year": prev_month.year,
    }

    urls = {
        "next_url" : False,
        "prev_url" : False,
    }
    if movies["page"] - 1 > 0:
        urls["prev_url"] = True
    if movies["total_pages"] - page > 0:
        urls["next_url"] = True

    return render_template("index.html", month_name=date(year, month, 1).strftime("%B"),
                           movies=movies["results"], page=page, **urls, **dates)

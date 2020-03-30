from app import app
from app.forms import NewsQueryForm
from datetime import date
from flask import render_template, flash, redirect, url_for
import requests

@app.route('/index', methods=['GET', 'POST'])
def index():
  form = NewsQueryForm()
  article_links = []
  if form.validate_on_submit():
    # Fetch news from NEWS-API
    api_key = '8d1893c68e274ad89f3b089704b5e566'
    # Current date
    date_today = date.today().strftime("%Y-%m-%d")
    url = ('http://newsapi.org/v2/everything?'
           f'q={form.search_query.data}&'
           f'from={date_today}&'
           'sortBy=popularity&'
           f'apiKey={api_key}&'
           'pageSize=30')
    response = requests.get(url)
    data = response.json()
    # keys : status, totalResults, articles
    status = data['status']
    if(status == "ok"):
        articles = data['articles']
        articles_fetched = len(articles)
        # list of links to articles
        article_links = [(article['title'], article['url'])
                         for article in articles]
        flash("Number of results fetched {}".format(articles_fetched))   
    else:
        flash("There was some error. Please search again")
  return render_template('index.html', title='Home', form=form, article_links=article_links)



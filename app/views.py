from flask import render_template
from app import app
from .request import get_news


#views
@app.route('/')
def index():
    '''
    view root page that returns the index page and its data
    '''


    title = "News Mania"


    all_news = get_news('all')
    print(all_news)


    return render_template('index.html', title= title, all = all_news)
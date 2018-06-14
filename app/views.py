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

    all_news = get_news('sports')
    general_news = get_news('general')
    tech_news = get_news('technology')

    # print(all_news)


    return render_template('index.html', title= title, sports = all_news, general = general_news, technology = tech_news)

# Views
@app.route('/news/<int:id>')
def news(id):
    '''
    View movie page function that returns the movie details page and its data
    '''
    news = get_news(id)

    
    return render_template('index.html', news = news)

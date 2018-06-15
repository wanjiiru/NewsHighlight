from flask import render_template
from app import app
from .request import get_news, get_articles


#views
@app.route('/')
def index():
    '''
    view root page that returns the index page and its data
    '''
    title = "Welcome to the best news point"

    all_news = get_news('sports')
    general_news = get_news('general')
    tech_news = get_news('technology')
    bus_news = get_news('business')
    ent_news = get_news('ent')
    sci_news = get_news('science')


    # print(all_news)


    return render_template('index.html', title= title, sports = all_news, general = general_news, technology = tech_news, busines = bus_news, ent = ent_news, science = sci_news)

# Views
@app.route('/news/<int:id>')
def news(id):
    '''
    View movie page function that returns the movie details page and its data
    '''
    news = get_news(id)

    
    return render_template('index.html', news = news)



@app.route('/articles/<source_id>')
def articles(source_id):
    '''
    function that returns articles by source id
    '''

    article_source = get_articles(source_id)
    title = f'{source_id}| Articles'
    return render_template('articles.html',title = title, name = source_id, news = article_source )


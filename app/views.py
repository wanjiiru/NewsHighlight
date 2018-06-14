from flask import render_template
from app import app


#views
@app.route('/')
def index():
    '''
    view root page that returns the index page and its data
    '''


    title = "News Mania"


    return render_template('index.html', title= title)
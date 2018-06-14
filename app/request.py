from app import app
import urllib.request, json
from . models import news

#getting api key
api_key = app.config['NEWS_API_KEY']

News=news.News
#getting the news base url
base_url = app.config['ALL_NEWS_API_URL']


def get_news(category):
    '''function that gets the json response to the url request
    '''
    get_news_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)

    return news_results


def process_results(news_list):
    '''
    '''

    news_results = []
    for news_item in news_list:
        name = news_item.get('name')
        author = news_item.get('author')
        country = news_item.get('country')
        description = news_item.get('description')
        category = news_item.get('category')

        if author:
            news_object = News(name, author, country, description, category)
            news_results.append(news_object)

    return news_results

        

        

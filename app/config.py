class Config:
    '''
    General configuration parent class
    '''
    ALL_NEWS_API_URL = 'https://newsapi.org/v2/everything?sources=bbc-news,al-jazeera-english,cnn,independent,google-news,bloomberg,engadget,espn,fortune&sortBy=publishedAt&pageSize={}&apiKey={}'




class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
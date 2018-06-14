class Articles:
    '''
    articles class to define article objects
    '''
    def __init__(self, title, description, urlToImage, publishedAt, author, url):
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.author = author
        self.url = url
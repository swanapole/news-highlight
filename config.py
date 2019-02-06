import os

class Config:
    '''
    General configuration parent class
    '''
    SOURCES_BASE_URL =" https://newsapi.org/v2/sources?language=en&apiKey=0f4ee6fd99a24df3826d0f34d3c08dab"
    EVERYTHING_BASE_URL="https://newsapi.org/v2/everything?sources={}s&apiKey=0f4ee6fd99a24df3826d0f34d3c08dab"
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    '''

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    

    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}

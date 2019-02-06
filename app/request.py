import urllib.request,json
from .models import Source
from .models import Article



# Getting api key
api_key = None
# Getting the movie base url
source_url = None
everything_url = None

def configure_request(app):
    global api_key,sources_url,everything_url
    api_key = app.config['NEWS_API_KEY']
    sources_url = app.config["SOURCES_BASE_URL"]
    everything_url= app.config["EVERYTHING_BASE_URL"]

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = sources_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)


    return source_results
def process_results(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain movie details

    Returns :
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')

        source_object = Source(id,name,description,url,category,language)
        source_results.append(source_object)

    return source_results

def get_articles(source_id):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = everything_url.format(category,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_sources_response['articles']
            articles_results = process_results(articles_results_list)


    return articles_results
def process_articles(articles_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        articles_list: A list of dictionaries that contain movie details

    Returns :
        articles_results: A list of source objects
    '''
    articles_results = []
    for article_item in articles_list:

        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')


        if urlToImage:
            articles_object = Articles(title, description, url, urlToImage)
            articles_results.append(articles_object)

    return articles_results

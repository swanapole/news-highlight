from flask import render_template,redirect,url_for,request
from . import main
from ..request import get_sources,get_articles
from ..models import Source,Article
# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting popular movie
    general_sources = get_sources('general')
    print(general_sources)
    title = 'news-highlight'
    return render_template('index.html', title = title,general = general_sources)

@main.route('/article/<source_id>')
def article(source_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    get_article = get_article(source_id)
    title = f'{source_id}'

    return render_template('article.html',title = title,id = source_id,article = article)

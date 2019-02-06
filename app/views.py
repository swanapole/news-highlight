from flask import render_template
from app import app
from .request import get_sources,get_articles
# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting popular movie
    general_sources = get_sources('general')
    print(general_sources)
    title = 'news-highlight'
    return render_template('index.html', title = title,general = general_sources)

@app.route('/article/<source_id>')
def article(source_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    get_article = get_article(source_id)
    title = f'{source_id}'

    return render_template('article.html',title = title,id = source_id,article = article)

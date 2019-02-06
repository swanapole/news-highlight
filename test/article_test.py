import unittest
from models import article
Article = article.Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article("Today in microfashion…","Today in microfashion…","http://www.humansofnewyork.com/post/182598016566/today-in-microfashion","https://66.media.tumblr.com/270d4fbd6f46fc8ec03e386969bc572a/tumblr_pmhobj60uz1qggwnvo1_500.jpg")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))


if __name__ == '__main__':
    unittest.main()

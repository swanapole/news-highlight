class Source:
    '''
    source class to define Movie Objects
    '''

    def __init__(self,id,name,description,url,category,language):
        self.id =id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language

class Article:
    '''
    Article class to define source Objects
    '''

    def __init__(self,id,name,description,url,category,language):
        self.title =title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage

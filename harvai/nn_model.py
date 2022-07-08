from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
from harvai.data import get_clean_preproc_data


class Nn_model():
    def __init__(self,article_number,digits=False):
        self.data = None
        self.model = None
        self.vectorizer = None
        self.articles = None
        self.articles_reference = None
        self.article_number = article_number
        self.digits = digits

    def clean_data(self):
        self.data = get_clean_preproc_data(self.digits)

    def fit(self):
        self.vectorizer = TfidfVectorizer(max_df=0.8)
        features = self.vectorizer.fit_transform(self.data.article_lemmatized)

        self.model = NearestNeighbors(n_neighbors=self.article_number)
        self.model.fit(features)

    def predict(self,question):
        input = self.vectorizer.transform([question])
        self.articles = list(self.model.kneighbors(input, return_distance=False)[0])

    def get_articles_parsed(self): # Liste d'articles
        articles_parsed = []
        article = self.articles[0:self.article_number]
        for i in article:
            articles_parsed.append(self.data.article_content[i])
        return articles_parsed

    def get_article_reference(self):
        articles_references = []
        articles = self.articles[0:self.article_number]
        for i in articles:
            articles_references.append(self.data.article_reference[i])
        return articles_references

    def get_articles_text_only (self):
        if len(self.articles)< self.article_number :
            article = self.articles
        else:
            article = self.articles[0:self.article_number]
        return ''.join(self.data.article_content[article])



if __name__ == "__main__":

    test = Nn_model(5)
    test.clean_data()
    test.fit()
    test.predict("Quelle est la peine pour conduite en état d'ivresse?")
    print(test.get_articles_parsed())
    print(test.get_article_reference())

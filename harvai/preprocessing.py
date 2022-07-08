import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
import simplemma
from nltk.stem.snowball import FrenchStemmer


def article_number(x):
    return x[:17]

def article_content(x):
    return x[17:]

def article_lower(x):
    x = x.lstrip()
    return x.lower()

def remove_numbers(x):
    return ''.join([i for i in x if not i.isdigit()])

def remove_punctuation(x):
    for punctuation in string.punctuation :
        x = x.replace(punctuation," ")
    return x

def remove_stopwords(x):
    stop_words = set(stopwords.words('french'))
    word_tokens = word_tokenize(x)
    x = [word for word in word_tokens if not word in stop_words]
    x = [word for word in x if len(word)>1]
    return x


def tfidf_format(x):
    x = " ".join([str(word) for word in x])
    return x

def Lemmatize(x):
    x = simplemma.text_lemmatizer(x,lang='fr')
    x = " ".join([str(word) for word in x])
    return x

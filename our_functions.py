
from nltk.corpus import stopwords 
from nltk.stem import PorterStemmer
from nltk.tokenize import RegexpTokenizer

def clean_text(text):
    stop_words = set(stopwords.words('english'))
    tokenizer = RegexpTokenizer("[a-z]+")
    tokens = tokenizer.tokenize(text.lower())
    result = [word for word in tokens if not word in stop_words]
    return tokens
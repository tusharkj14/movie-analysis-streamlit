import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

porter = PorterStemmer()
def text_processing(data):
    nopunc = [i for i in data.lower() if i not in string.punctuation]
    nopunc = ''.join(nopunc)
    return [porter.stem(i) for i in nopunc.split() if i not in stopwords.words('English') and len(i)>3]
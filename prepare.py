import unicodedata
import re
import json

import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

import pandas as pd

import acquire


def basic_clean(string):
    # converting string to lowercase
    string = string.lower()
    
    # encoding string to ASCII, to convert special characters
    # Decode from ASCII to UTF-8 so we have normal python string
    string = unicodedata.normalize('NFKD', string)\
    .encode('ascii', 'ignore')\
    .decode('utf-8', 'ignore')
    
    # Remove any special characters and replace with an empty string
    string = re.sub(r"[^a-z0-9'\s]", '', string)

    return string


def tokenize(string):
    # initializing tokenizer
    tokenizer = nltk.tokenize.Toktoktokenizer()
    
    # using the tokenizer
    string = tokenizer.tokenize(string, return_str=True)
    
    return string

def stem(string):
    # Initializing Porter Stemmer
    ps = nltk.porter.PorterStemmer()
    
    # creating our list of stems
    stems = [ps.stem(word) for word in string.split()]
    
    # Unpacking our list
    stem_string = ' '.join(stems)

    return stem_string


def lemmatize(string):
    # Initializing our Word Net Lemmatizer
    wnl = nltk.stem.WordNetLemmatizer()
    
    # applying lemmatization to our string
    lemmas = [wnl.lemmatize(word) for word in string.split()]
    string_lemmatized = ' '.join(lemmas)
    
    return string_lemmatized


def remove_stopwords(string, extra_words=[], exclude_words=[]):
    # setting up stop words list from nltk
    stopword_list = stopwords.words('english')
    
    # Adding/Filtering extra words to stopword list
    words = string.split()
    stopword_list = stopword_list + extra_words
    stopword_list = stopword_list - exclude_words
    filtered_words = [w for w in words if w not in stopword_list]
    
    # Now we remove the stop words from our string
    print('Removed {} stopwords'.format(len(words) - len(filtered_words)))
    print('---')

    string_without_stopwords = ' '.join(filtered_words)

    return string_without_stopwords

    
    
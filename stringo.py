import numpy as np
import pandas as pd
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
from nltk.corpus import wordnet
stemmer = SnowballStemmer('english')
import spacy
nlp = spacy.load('en_core_web_lg')
import re
import string

def apply_function_typewise(obj='', function='', col_names=''):
    """
    Apply the function for a given input
    """
    obj_type = type(obj)
    
    if obj_type == str:
        return function(obj)
    
    elif (obj_type==np.ndarray) or (obj_type==list):
        return list(map(function, obj))
    
    elif obj_type==pd.DataFrame:
        column_names = obj.columns
        if col_names != '':
            column_names = col_names
        return pd.DataFrame([obj[col].map(function) for col in column_names]).T
    
    elif obj_type==pd.Series:
        return obj.map(function)
    
    else:
        return obj
    
def lemmatize_object(obj='', col_names=''):
    """
    The function can be used to lemmatize the strings for a given input.
    
    INPUT: Single String, Array or List of Strings, DataFrame or a Series Object.
    OUTPUT: Lemmatized strings retaining the original data structure.
    
    Comments: In case of DataFrame Object. You can also specify the column names. Default it will
    run on all columns.
    """
    
    function=lambda x: WordNetLemmatizer().lemmatize(x,'v')
    return apply_function_typewise(obj, function, col_names)


def stem_object(obj='', col_names=''):
    """
    The function can be used to stem the strings for a given input.
    
    INPUT: Single String, Array or List of Strings, DataFrame or a Series Object.
    OUTPUT: Stemmed strings retaining the original data structure.
    
    Comments: In case of DataFrame Object. You can also specify the column names. Default it will
    run on all columns.
    """
    
    function=lambda x: stemmer.stem(x)
    return apply_function_typewise(obj, function, col_names)
    


def remove_extra_spaces(obj='', col_names=''):
    """
    The function can be used to remove extra spaces from the strings for a given input.
    
    INPUT: Single String, Array or List of Strings, DataFrame or a Series Object.
    OUTPUT: Removed extra spaces strings retaining the original data structure.
    
    Comments: In case of DataFrame Object. You can also specify the column names. Default it will
    run on all columns.
    """
    
    function=lambda x: re.sub('\s\s+',' ', x).strip()
    return apply_function_typewise(obj, function, col_names)


def split_sentences_spacy(obj='', col_names=''):
    """
    INPUT: Long Sentence
    OUTPUT: Array of Sub-Sentences 
    """
    
    reaesc = re.compile(r'\x1b[^m]*m')
    function = lambda x: [reaesc.sub('', sent.text).strip() for sent in nlp(re.sub('\\n','. ', x)).sents]
    return apply_function_typewise(obj, function, col_names)

 
def remove_symbols(x_text):
    for p in string.punctuation:
        x_text = x_text.replace(p,' ')
    return remove_extra_spaces(x_text)

def remove_punctuations(obj='', col_names=''):
    """
    INPUT: Single String, Array or List of Strings, DataFrame or a Series Object.
    OUTPUT: Removed punctuation marks from strings retaining the original data structure.
    """
    
    return apply_function_typewise(obj, remove_symbols, col_names)


def remove_empty_from_list(obj='', col_names=''):
    
    """
    INPUT: Single String, Array or List of Strings, DataFrame or a Series Object.
    OUTPUT: Removed empty ('') marks from list retaining the original data structure.
    """
    
    function = lambda x: np.delete(np.asarray(x), np.where(np.asarray(x)=='')).tolist()
    if type(obj)==list:
        obj=[obj]
        return apply_function_typewise(obj, function, col_names)[0]
        
    return apply_function_typewise(obj, function, col_names)



def sort_list_of_strings(obj='', col_names='', reverse=False):
    
    """
    Sort the Given Object (having strings) according to the length 
    
    INPUT: Single String, Array or List of Strings, DataFrame or a Series Object.
    OUTPUT: sorted list retaining the original data structure.
    """
    
    function = lambda x: sorted(x, key=len, reverse=reverse)  if type(x)==list else x
    if type(obj)==list:
        return function(obj)
    
    return apply_function_typewise(obj, function, col_names)


def tokenize_string_spacy(obj='', col_names=''):
    
    """
    Tokenize (break into words) the Given Object (having strings) using spacy tokenizer
    
    INPUT: Single String, Array or List of Strings, DataFrame or a Series Object.
    OUTPUT: sorted list retaining the original data structure.
    """    
    
    
    function = lambda x: [token.text for token in nlp(x)]
    return apply_function_typewise(obj, function, col_names)


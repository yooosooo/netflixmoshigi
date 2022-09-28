import nltk
import pickle
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

import re
nltk.download('all')
nltk.download('punkt')
nltk.download('wordnet')

with open('newproject\juman.txt', 'r') as f:
    content = f.read()

cleaned_content = re.sub(r'[^\.\?\!\w\d\s]','',content)
#print(cleaned_content)

cleaned_content = cleaned_content.lower()

word_tokens = nltk.word_tokenize(cleaned_content)
#print(word_tokens)

tokens_pos = nltk.pos_tag(word_tokens)
#print(tokens_pos)

from nltk.corpus import wordnet

def get_wordnet_pos(word):
    """Map POS tag to first character lemmatize() accepts"""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)

lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in word_tokens]

#print(lemmatized_words)

stopwords_list = stopwords.words('english')

unique_words = set(lemmatized_words)
final_words = lemmatized_words
for word in unique_words:
    if word in stopwords_list:
        while word in final_words: final_words.remove(word)

#print(final_words)

def remove_punc(string):
    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    for ele in string:  
        if ele in punc:  
            string = string.replace(ele, "") 
    return string
 
lis = [remove_punc(i) for i in final_words]
#print(lis) 
 
str_list = list(filter(None, lis))
print(str_list)
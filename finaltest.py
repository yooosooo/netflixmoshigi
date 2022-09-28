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

cleaned_content = content.lower()

stopwords_list = stopwords.words('english')

unique_words = set(cleaned_content)
final_words = cleaned_content
for word in unique_words:
    if word in stopwords_list:
        while word in final_words: final_words.remove(word)

good_content = re.sub(r'[^\.\?\!\w\d\s]','',final_words)

word_tokens = nltk.word_tokenize(good_content)
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
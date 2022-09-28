import nltk
import pickle
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('averaged_perceptron_tagger')

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

lemmatizer = WordNetLemmatizer()

def pos_tagger(nltk_tag):
    if nltk_tag.startswith('J'):
        return wordnet.ADJ
    elif nltk_tag.startswith('V'):
        return wordnet.VERB
    elif nltk_tag.startswith('N'):
        return wordnet.NOUN
    elif nltk_tag.startswith('R'):
        return wordnet.ADV
    else:         
        return None

  
lemmatized_words = [lemmatizer.lemmatize(w, pos_tagger(w)) for w in word_tokens]



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
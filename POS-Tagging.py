import nltk 
nltk.download('punkt')
from nltk import pos_tag, word_tokenize

# Tag parts of the speech (POS)
sentence = word_tokenize("I always lie down to tell a lie.")
print(pos_tag(sentence))


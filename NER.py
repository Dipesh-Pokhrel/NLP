from nltk import pos_tag, ne_chunk
from nltk.tokenize import word_tokenize

# Recognize name entities in a tagged sentence
ne_chunk(pos_tag(word_tokenize("Antonio joined Fc. Chelsea in UK.")))
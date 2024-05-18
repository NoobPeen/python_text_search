import re
import spacy

nlp = spacy.load("en_core_web_sm")

def tokenize(text):
    if text is None:
        return []
    return re.findall(r'\b\w+\b', text)

def lowercase_filter(tokens):
    return [token.lower() for token in tokens]

def stopword_filter(tokens):
    stopwords = set(["and", "the", "is", "in", "at", "of"])
    return [token for token in tokens if token not in stopwords]

def stemmer_filter(tokens):
    doc = nlp(" ".join(tokens))
    return [token.lemma_ for token in doc]

def analyze(text):
    tokens = tokenize(text)
    tokens = lowercase_filter(tokens)
    tokens = stopword_filter(tokens)
    tokens = stemmer_filter(tokens)
    return tokens

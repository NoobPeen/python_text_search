import spacy
nlp = spacy.load("en_core_web_sm")


def lowercaseFilter(tokens):
    return [token.lower() for token in tokens]

def stopwordFilter(tokens):
    return [token for token in tokens if not nlp.vocab[token].is_stop]

def stemmerFilter(tokens):
    doc = nlp(" ".join(tokens))
    return [token.lemma_ for token in doc]

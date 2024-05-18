from Utils.text_tokenize import analyze
from collections import defaultdict
import logging

class Index:
    def __init__(self):
        self.index = defaultdict(list)
    
    def add(self, docs):
        logging.info("Starting to index documents")
        for doc in docs:
            logging.debug(f"Indexing document ID: {doc.id}")
            tokens = analyze(doc.text)
            logging.debug(f"Tokens for document ID {doc.id}: {tokens}")
            for token in tokens:
                if self.index[token] and self.index[token][-1] == doc.id:
                    continue
                self.index[token].append(doc.id)
        logging.info("Completed indexing documents")
    
    def search(self, text):
        result = None
        tokens = analyze(text)
        logging.info(f"Searching for tokens: {tokens}")
        for token in tokens:
            if token in self.index:
                if result is None:
                    result = set(self.index[token])
                else:
                    result.intersection_update(self.index[token])
            else:
                logging.info(f"Token '{token}' not found in index")
                return []
        return list(result) if result else []

    def print_index(self):
        for token, ids in self.index.items():
            print(f"Token: {token}, IDs: {ids}")

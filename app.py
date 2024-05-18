import argparse
import logging
import time
from Utils.load_documents import load_documents
from Utils.index_doc import Index

def main():
    parser = argparse.ArgumentParser(description="Full Text Search Engine")
    parser.add_argument('-p', '--path', default='enwiki-latest-abstract1.xml.gz', help='Wiki abstract dump path')
    parser.add_argument('-q', '--query', default='', help='Search query')
    args = parser.parse_args()

    dump_path = args.path
    query = args.query

    if not query:
        query = input("Please enter your search query: ")

    logging.basicConfig(level=logging.INFO)
    logging.info("Running Full Text Search")

    start = time.time()
    docs = load_documents(dump_path)
    logging.info(f"Loaded {len(docs)} documents in {time.time() - start:.2f} seconds")

    start = time.time()
    index = Index()
    
    batch_size = 1000
    for i in range(0, len(docs), batch_size):
        logging.info(f"Indexing batch {i} to {i + batch_size}")
        index.add(docs[i:i + batch_size])
    
    logging.info(f"Indexed {len(docs)} documents in {time.time() - start:.2f} seconds")

    start = time.time()
    matched_ids = index.search(query)
    logging.info(f"Search found {len(matched_ids)} documents in {time.time() - start:.2f} seconds")

    for doc_id in matched_ids:
        doc = docs[doc_id]
        logging.info(f"{doc_id}\t{doc.text}")

if __name__ == "__main__":
    main()

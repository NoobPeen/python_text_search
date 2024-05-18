import gzip
import xml.etree.ElementTree as ET

class Document:
    def __init__(self, title, url, text, doc_id):
        self.title = title
        self.url = url
        self.text = text
        self.id = doc_id

def load_documents(path):
    try:
        # Open the gzipped file
        with gzip.open(path, 'rb') as f:
            # Parse the XML data
            tree = ET.parse(f)
            root = tree.getroot()
            c=0
            documents = []
            for i, doc in enumerate(root.findall('doc')):
                title_element = doc.find('title')
                url_element = doc.find('url')
                text_element = doc.find('abstract')
                
                title = title_element.text if title_element is not None else ""
                url = url_element.text if url_element is not None else ""
                text = text_element.text if text_element is not None else ""
                
                documents.append(Document(title, url, text, i))
                
            return documents
    except Exception as e:
        print(f"Error loading documents: {e}")
        return []

# # Example usage
# file_path = 'enwiki-latest-abstract1.xml.gz'
# documents = load_documents(file_path)
# i=0
# for doc in documents:
#     print(f"ID: {doc.id}, Title: {doc.title}, URL: {doc.url}, Text: {doc.text[:100]}...") 
#     i+=1
#     if i==10:
#         break
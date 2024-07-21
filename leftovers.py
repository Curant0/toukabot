'''
class OpenAIEmbeddings:
    def __init__(self, api_key: str, model: str = "text-embedding-3-small"):
        openai.api_key = api_key
        self.model = model

    def embed_documents(self, documents: List[str]) -> List[List[float]]:
        embeddings = []
        for document in documents:
            response = openai.Embedding.create(input=document, model=self.model)
            embeddings.append(response['data'][0]['embedding'])
        return embeddings

    def embed_query(self, query: str) -> List[float]:
        response = openai.Embedding.create(input=query, model=self.model)
        return response['data'][0]['embedding']
'''

'''
# Function to load .txt documents from a directory
def load_text_documents(directory):
    documents = []
    for filepath in glob.glob(f"{directory}/*.txt"):
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            documents.append(Document(page_content=content))
    return documents
    '''




'''
# Function to initialize and load documents into Chroma
def initialize_chroma_with_documents(documents):
    embeddings = JinaAIEmbeddings()
    # Embed all documents
    embedded_docs = [embeddings.embed_documents([doc.page_content])[0] for doc in documents]
    # Load embedded documents into Chroma
    chroma_db = Chroma.from_documents(embedded_docs, embeddings)
    return chroma_db

# Function to initialize and load documents into Chroma
def initialize_chroma_with_documents(documents):
    # Directly use the documents' page_content for Chroma, assuming they are Document objects
    chroma_db = Chroma.from_documents(documents, JinaAIEmbeddings())
    return chroma_db
 '''
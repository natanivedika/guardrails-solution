import chromadb
from sentence_transformers import SentenceTransformer

class SemanticDetector:
    """Create a client, use a model to convert text to vectors, and get a db collection."""
    def __init__(self):
        self.client = chromadb.Client() # create a client
        self.model = SentenceTransformer("all-MiniLM-L6-v2") # convert text to vectors
        self.collection = self.client.get_or_create_collection("rules") # get db collection (check)

        if self.collection.count() == 0:
            self._seed()

    """seeding the db: if the collection is empty, add three example rules to (1.) detect text about patient diagnosis or lab results, (2.) detect text about sharing ssn, and (3.) detect sharing credit card numbers"""
    def _seed(self):
        rules = [
            ("phi", "patient diagnosis or lab results", "block"),
            ("ssn", "sharing social security number", "mask"),
            ("credit", "sharing credit card number", "mask")
        ]
        for i, (rid, text, action) in enumerate(rules):
            emb = self.model.encode(text).tolist()
            self.collection.add(
                ids=[rid],
                documents=[text],
                metadatas=[{"action": action}],
                embeddings=[emb]
            )

    """When text is passed, convert it to vector embedding, find a rule in the db collection that is most similar to the text. If the similarity distance is very similar (<0.25), return the appropriate action. Return None if no similar rule is found."""
    def detect(self, text):
        emb = self.model.encode(text).tolist()
        res = self.collection.query(query_embeddings=[emb], n_results=1)
        if res["distances"][0][0] < 0.25:
            return res["metadatas"][0][0]
        return None

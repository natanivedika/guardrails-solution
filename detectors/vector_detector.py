import chromadb
from detectors.base import Detector
from models.violation import Violation
from config.settings import Settings

# initialize ChromaDB client and collection
client = chromadb.Client()
collection = client.get_or_create_collection("aigenie_kb")

class VectorDetector(Detector):
    """
    Detects semantic similarity violations using vector embeddings.

    This detector uses ChromaDB to perform semantic search, comparing the
    input text against a knowledge base of embedded content. If the cosine
    similarity score meets or exceeds the configured threshold, the entire
    input is flagged as a violation.
    """

    def detect(self, text):
        res = collection.query(query_texts=[text], n_results=1)
        score = res["distances"][0][0]

        if score >= Settings.VECTOR_SIM_THRESHOLD:
            return [
                Violation(
                    constraint_id=self.constraint.constraint_id,
                    type="semantic",
                    severity=self.constraint.attributes.get("severity", 7),
                    start=0,
                    end=len(text)
                )
            ]
        return []

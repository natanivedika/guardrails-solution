import spacy
from presidio_analyzer import AnalyzerEngine

class NERDetector:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.presidio = AnalyzerEngine()

    def detect(self, text):
        hits = []

        # store detected spaCy entities
        doc = self.nlp(text)

        # iterate through the detected entities
        for ent in doc.ents:
            # check if the entity is a relevant type for PHI detection (names, locations, organizations, dates)
            # and add to list with the metadata
            if ent.label_ in {"PERSON", "GPE", "ORG", "DATE"}:
                hits.append({
                    "type": ent.label_,      # entity category
                    "start": ent.start_char, # start position
                    "end": ent.end_char,     # end position
                    "confidence": 0.7        # detection conf
                })

        # PHI - presidio
        results = self.presidio.analyze(text=text, language="en")
        for r in results:
            hits.append({
                "type": r.entity_type,
                "start": r.start,
                "end": r.end,
                "confidence": r.score
            })

        return hits
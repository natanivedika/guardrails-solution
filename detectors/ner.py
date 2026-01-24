import spacy
from presidio_analyzer import AnalyzerEngine

nlp = spacy.load("en_core_web_lg")
analyzer = AnalyzerEngine()


class NERDetector:
    """documentation"""
    def detect(self, text):

        # store detected spaCy entities
        doc = nlp(text)
        ents = [{"text": e.text, "label": e.label_} for e in doc.ents]

        pii = analyzer.analyze(text, language="en")
        for p in pii:
            ents.append({"text": text[p.start:p.end], "label": p.entity_type})
        
        return ents
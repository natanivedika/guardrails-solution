import spacy
from detectors.base import Detector
from models.violation import Violation

# load spaCy model once at module level to avoid reloading
_nlp = spacy.load("en_core_web_sm")

class SpacyDetector(Detector):
    """
    Detects named entities in text using spaCy's pre-trained NLP model.

    This detector identifies specific entity types (e.g., PERSON, ORG, GPE,
    DATE) that are listed in the constraint's "entities" attribute. When a
    matching entity is found, it's flagged as a violation with the configured
    severity level.
    """






    def detect(self, text):
        doc = _nlp(text)
        violations = []
        allowed = set(self.constraint.attributes.get("entities", []))
        severity = self.constraint.attributes.get("severity", 5)

        for ent in doc.ents:
            if ent.label_ in allowed:
                violations.append(
                    Violation(
                        constraint_id=self.constraint.constraint_id,
                        type=ent.label_,
                        severity=severity,
                        start=ent.start_char,
                        end=ent.end_char
                    )
                )
        return violations

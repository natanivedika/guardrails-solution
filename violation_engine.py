from detectors.spacy_detector import SpacyDetector
from detectors.regex_detector import RegexDetector
from detectors.vector_detector import VectorDetector

DETECTORS = {
    "spacy": SpacyDetector,
    "regex": RegexDetector,
    "vector": VectorDetector
}

class ViolationEngine:
    """
    Orchestrates multiple detectors to scan text for constraint violations.

    Initialized with a list of constraints and instantiates
    the appropriate detector for each one based on its constraint_type. When
    detecting violations, it runs all detectors in sequence and aggregates their
    results.
    """

    def __init__(self, constraints):
        """
        Initializes the engine with detectors for each constraint.
        """

        self.detectors = []
        for c in constraints:
            detector = DETECTORS[c.constraint_type](c)
            self.detectors.append(detector)

    def detect(self, text):
        """
        Runs all detectors against the input text and aggregates violations.
        """
        
        violations = []
        for d in self.detectors:
            violations.extend(d.detect(text))
        return violations

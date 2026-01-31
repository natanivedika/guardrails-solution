import re
from detectors.base import Detector
from models.violation import Violation

class RegexDetector(Detector):
    """
    Detects pattern matches in text using regular expressions.

    This detector compiles a list of regex patterns from the constraint's
    attributes and flags any matches found in the input text as violations.
    """

    def __init__(self, constraint):
        """
        Initializes the detector and pre-compiles all regex patterns.
        """

        super().__init__(constraint)
        self.patterns = [
            re.compile(p) for p in constraint.attributes.get("patterns", [])
        ]

    def detect(self, text):
        """
        Scans text for matches against all configured regex patterns.
        """
        
        violations = []
        severity = self.constraint.attributes.get("severity", 5)

        for pattern in self.patterns:
            for m in pattern.finditer(text):
                violations.append(
                    Violation(
                        constraint_id=self.constraint.constraint_id,
                        type="regex",
                        severity=severity,
                        start=m.start(),
                        end=m.end()
                    )
                )
        return violations

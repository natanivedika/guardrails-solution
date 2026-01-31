from abc import ABC, abstractmethod
from typing import List
from models.violation import Violation

class Detector(ABC):
    """
    Abstract base class for all constraint detectors.

    Detectors implement specific violation detection logic for different
    constraint types. Each concrete detector subclass is responsible for
    scanning user input text and identifying instances where a particular
    constraint is violated.

    Subclasses must implement the `detect` method to define how violations
    are identified and reported for their specific constraint type.
    """





    def __init__(self, constraint):
        self.constraint = constraint

    @abstractmethod
    def detect(self, text: str) -> List[Violation]:
        pass

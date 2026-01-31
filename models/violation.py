from uuid import UUID

class Violation:
    """
    Represents a single constraint violation detected in user input.

    Captures metadata about a specific violation, including
    which constraint was triggered, the type of violation, its severity,
    and the character span in the input where it occurred.
    """
    
    constraint_id: UUID
    type: str
    severity: int
    start: int
    end: int


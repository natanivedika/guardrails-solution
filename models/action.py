from enum import Enum

class Action(Enum):
    """
    Defines the possible actions the system can take in response to a
    policy or guardrail evaluation.

    PASS: The request is allowed through with no intervention.
    RESTRICTED: The request is permitted but flagged or modified
            before proceeding (e.g., redacted, logged, or requiring
            additional review).
    STOP: The request is fully blocked and does not proceed further.
    """

    PASS = "pass"
    RESTRICTED = "restricted"
    STOP = "stop"

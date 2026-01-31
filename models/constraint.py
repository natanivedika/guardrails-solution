from uuid import UUID

class Constraint:
    """
    Represents a single constraint rule from the aigenie_policies.constraints table.
    """

    constraint_id: UUID
    constraint_type: str
    attributes: dict

from models.action import Action

class Enforcer:
    """
    Determines the appropriate enforcement action based on detected violations and policy rules.
    """

    def decide(self, violations, policy):
        if not violations:
            return Action.PASS

        max_sev = max(v.severity for v in violations)

        if policy["policy_type"] == "stop":
            return Action.STOP

        if max_sev >= 6:
            return Action.RESTRICTED

        return Action.PASS

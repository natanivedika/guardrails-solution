from enforcer import Enforcer
from masker import Masker
from hitl import human_decision
from models.action import Action

class StreamGuardrail:
    """
    Guardrail system for processing streaming text chunks.

    Applies policy-based violation detection and enforcement to
    individual chunks of streaming content (e.g., LLM responses being generated
    token-by-token). Each chunk is scanned for violations, and the appropriate
    action (pass, mask, or stop) is taken based on the policy configuration.
    """

    def __init__(self, policy, engine):
        """
        Initializes the guardrail with policy rules and a violation engine.
        """

        self.policy = policy
        self.engine = engine
        self.enforcer = Enforcer()
        self.masker = Masker()

    async def process_chunk(self, chunk: str):
        """
        Scans a streaming chunk for violations and applies enforcement.
        """

        violations = self.engine.detect(chunk) # run all detectors on this chunk
        decision = self.enforcer.decide(violations, self.policy)

        if decision == Action.PASS:
            return chunk

        if decision == Action.RESTRICTED:
            masked = self.masker.mask(chunk, violations)
            allow = await human_decision({
                "chunk": chunk,
                "violations": violations
            })
            return chunk if allow else masked

        if decision == Action.STOP:
            raise RuntimeError("Streaming stopped due to policy violation")

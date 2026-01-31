import asyncio
from postgres import get_policies, get_constraints
from violation_engine import ViolationEngine
from guardrail import StreamGuardrail
from models.constraint import Constraint

async def run():
    subdomain_id = "83376a38-783a-4789-8eb4-21966b1ccd01"
    country = "USA"

    policies = get_policies(subdomain_id, country)
    constraints_raw = get_constraints(subdomain_id, country)

    policy = policies[0]

    constraints = [
        Constraint(
            constraint_id=c["constraint_id"],
            constraint_type=c["constraint_type"],
            attributes=c["attributes"]
        )
        for c in constraints_raw
    ]

    engine = ViolationEngine(constraints)
    guardrail = StreamGuardrail(policy, engine)

    async for chunk in fake_stream():
        output = await guardrail.process_chunk(chunk)
        print(output, end="", flush=True)

async def fake_stream():
    for c in ["Patient John Smith ", "was diagnosed with cancer."]:
        yield c

asyncio.run(run())

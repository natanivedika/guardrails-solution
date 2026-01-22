from collections import deque
from detectors.regex_detector import detect as regex_detect
from detectors.semantic import SemanticDetector
from masker import mask
from decision import decide

semantic = SemanticDetector()

def stream_guard(stream):
    buffer = deque(maxlen=120)

    for chunk in stream:
        buffer.extend(chunk)
        text = "".join(buffer)

        regex_hits = regex_detect(text)
        semantic_hit = semantic.detect(text) if regex_hits else None

        action = decide(regex_hits, semantic_hit)

        if action == "BLOCK":
            yield "[BLOCKED]"
            break
        elif action == "MASK":
            yield mask(chunk, regex_hits)
        else:
            yield chunk

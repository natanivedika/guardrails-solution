from collections import deque
from detectors.regex_detector import detect as regex_detect
from detectors.semantic import SemanticDetector
from masker import mask
from decision import decide

semantic = SemanticDetector()

def stream_guard(stream):
    buffer = deque(maxlen=120)

    for chunk in stream:
        prev_len = len(buffer) # track where new chunk begins in buffer
        buffer.extend(chunk)
        text = "".join(buffer)

        regex_hits = regex_detect(text)
        semantic_hit = semantic.detect(text) if regex_hits else None

        action = decide(regex_hits, semantic_hit)

        if action == "BLOCK":
            yield "[BLOCKED]"
            break
        elif action == "MASK":
            masked = list(chunk)

            for h in regex_hits:
                # map buffer index to chunk index: right-indexing for proper masking
                start = h["start"] - prev_len
                end   = h["end"]   - prev_len

                for i in range(max(0,start), min(len(chunk), end)):
                    masked[i] = "*"

            yield "".join(masked)
        else:
            yield chunk

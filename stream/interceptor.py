from collections import deque
from detectors.regex_detector import detect as regex_detect
from detectors.semantic import SemanticDetector
from detectors.ner import NERDetector
from masker import mask
from decision import decide

import time

semantic = SemanticDetector()
ner = NERDetector()

def stream_guard(stream):
    buffer = deque(maxlen=120)

    for chunk in stream:

        start_time = time.perf_counter() # START TIME

        prev_len = len(buffer) # track where new chunk begins in buffer
        buffer.extend(chunk)
        text = "".join(buffer)

        regex_hits = regex_detect(text)
        semantic_hit = semantic.detect(text)
        ner_hits = ner.detect(text)

        action = decide(regex_hits, semantic_hit, ner_hits)

        if action == "BLOCK":
            yield "[BLOCKED]"

            print(f"[Latency {(time.perf_counter()-start_time)*1000:.1f} ms]")

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

            print(f"[Latency {(time.perf_counter()-start_time)*1000:.1f} ms]")

        else:
            
            print(f"[Latency {(time.perf_counter()-start_time)*1000:.1f} ms]")

            yield chunk

import regex as re

# ssn pattern
SSN = re.compile(r"\b\d{3}-\d{2}-\d{4}\b")

# credit card pattern
CC  = re.compile(r"\b(?:\d[ -]*?){13,16}\b")

def detect(text):
    hits = []
    for pat, name in [(SSN,"ssn"),(CC,"credit_card")]:
        for m in pat.finditer(text):
            hits.append({"type": name, "start": m.start(), "end": m.end()})
    return hits
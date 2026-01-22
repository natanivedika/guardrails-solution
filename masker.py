def mask(text, spans):
    out = list(text)
    for s in spans:
        for i in range(s["start"], s["end"]):
            out[i] = "*"
    return "".join(out)
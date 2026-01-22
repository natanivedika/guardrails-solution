def decide(detections, semantic):
    if semantic and semantic["action"] == "block":
        return "BLOCK"
    if detections:
        return "MASK"
    return "ALLOW"
def decide(regex_hits, semantic_hit, ner_hits):
    if semantic_hit and semantic_hit["action"] == "block":
        return "BLOCK"
    
    if ner_hits:
        return "BLOCK"
    
    if regex_hits:
        return "MASK"
    
    return "ALLOW"
def decide(regex_hits, semantic_hit, ner_hits, has_medical_context):
    if semantic_hit and semantic_hit["action"] == "block":
        return "BLOCK"
    
    if has_medical_context and ner_hits:
        return "BLOCK"
    
    if regex_hits:
        return "MASK"
    
    return "ALLOW"
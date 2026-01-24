class GuardrailEngine:
   
   def  __init__(self, policy, ner_engine):
      self.policy = policy
      self.ner = ner_engine
      self.detected = []
      self.state = "PASS_THROUGH"

   """Scan a chunk of text and return the guardrail state.
      - detect entities in text chunk
      - store entity-level policy rule
      - calculate state based on the rank assignments"""
   def scan_text(self, text_chunk):
      entities = self.ner.detect(text_chunk)
      
      for ent in entities:
         if ent.label in self.policy["entities"]:
            rule = self.policy["entities"][ent.label]
            self.detected.append(ent)
            self.state = max(self.state, rule["level"], key=self.rank)

      for combination in self.policy["combinations"]:
         if all(x in [e.label for e in self.detected] for x in combination["if"]):
            self.state = combination["then"]
      
      return self.state
   
   """Assign rank to each level."""
   def rank(self, level):
      return {"PASS_THROUGH": 0, "RESTRICTED": 1, "STOP": 2}[level]
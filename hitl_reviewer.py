"""Display warning that sensitive entities are detected, display original text for reviewer,
    prompt reviewer to decide whether or not to allow unmasked version.
    Return TRUE if reviewer approves."""
def human_review(masked_text, ents):
    print("Sensitive data detected:")
    for e in ents:
        print(f"- {e['label']}: {e['text']}")

    print("\nMasked version:\n", masked_text)
    reviewer_decision = input("Allow unmasked? (yes/no): ")
    return reviewer_decision.lower() == "yes"
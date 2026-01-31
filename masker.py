class Masker:
    """
    Masks sensitive or violating content in text by replacing characters with asterisks.
    """

    def mask(self, text, violations):
        """
        Replaces characters at violation positions with asterisks.
        """

        chars = list(text)
        for v in violations:
            for i in range(v.start, v.end):
                chars[i] = "*"
        return "".join(chars)

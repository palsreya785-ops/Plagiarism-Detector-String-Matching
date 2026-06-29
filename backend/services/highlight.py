from difflib import SequenceMatcher


class Highlighter:

    def compare_sentences(self, original, submitted):

        original_sentences = original.split(".")

        submitted_sentences = submitted.split(".")

        matches = []

        for o in original_sentences:

            o = o.strip()

            if not o:
                continue

            for s in submitted_sentences:

                s = s.strip()

                if not s:
                    continue

                similarity = SequenceMatcher(
                    None,
                    o.lower(),
                    s.lower()
                ).ratio()

                if similarity >= 0.60:

                    matches.append({

                        "original_sentence": o,

                        "submitted_sentence": s,

                        "similarity": round(
                            similarity * 100,
                            2
                        )

                    })

        return matches
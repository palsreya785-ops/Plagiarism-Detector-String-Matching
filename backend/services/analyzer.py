from services.preprocessing import TextPreprocessor
from services.scoring import PlagiarismScorer
from services.highlight import Highlighter

from algorithms.naive import naive_search
from algorithms.kmp import kmp_search
from algorithms.rabin_karp import rabin_karp


def analyze_documents(original_text, submitted_text):

    pre = TextPreprocessor()

    original_text, _ = pre.normalize(original_text)
    submitted_text, _ = pre.normalize(submitted_text)

    original_words = set(original_text.split())

    matched = []

    for word in original_words:

        if len(word) < 4:
            continue

        if (
            naive_search(submitted_text, word)
            or kmp_search(submitted_text, word)
            or rabin_karp(submitted_text, word)
        ):
            matched.append(word)

    scorer = PlagiarismScorer()

    result = scorer.calculate(
        total_words=len(original_words),
        matched_words=len(matched)
    )

    result["matched_words"] = matched

    highlighter = Highlighter()
    result["matched_sentences"] = highlighter.compare_sentences(
        original_text,
        submitted_text
    )

    return result
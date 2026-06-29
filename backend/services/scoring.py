class PlagiarismScorer:

    def calculate(self, total_words, matched_words):

        if total_words == 0:
            percentage = 0
        else:
            percentage = round((matched_words / total_words) * 100, 2)

        if percentage >= 80:
            risk = "High"
        elif percentage >= 50:
            risk = "Medium"
        elif percentage >= 20:
            risk = "Low"
        else:
            risk = "Very Low"

        return {
            "overall_score": percentage,
            "risk_level": risk
        }
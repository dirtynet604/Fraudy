class RiskEngine:

    def calculate(
        self,
        header_findings,
        url_findings,
        attachment_findings,
        semantic_findings
    ):

        score = 0

        score += len(header_findings) * 15

        score += len(url_findings) * 10

        score += len(attachment_findings) * 20

        score += semantic_findings.get(
            "phishing_probability",
            0
        )

        return min(score, 100)
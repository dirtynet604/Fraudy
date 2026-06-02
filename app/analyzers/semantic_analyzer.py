from llm.ensemble import LLMEnsemble

class SemanticAnalyzer:

    def __init__(self):
        self.ensemble = LLMEnsemble()

    def analyze(self, email_data):

        prompt = f"""
Analyze the following email.

BODY:
{email_data.body}

Identify:

1. Phishing indicators
2. Social engineering tactics
3. Credential theft attempts
4. Urgency manipulation
5. Financial fraud patterns
6. Business Email Compromise indicators

Return JSON only.
"""

        return self.ensemble.analyze(prompt)
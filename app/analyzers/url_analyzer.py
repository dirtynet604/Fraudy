import tldextract

class URLAnalyzer:

    SUSPICIOUS_TLDS = [
        "xyz",
        "top",
        "click",
        "live",
        "shop"
    ]

    def analyze(self, urls):

        findings = []

        for url in urls:

            ext = tldextract.extract(url)

            if ext.suffix in self.SUSPICIOUS_TLDS:
                findings.append(
                    f"Suspicious TLD: {url}"
                )

        return findings
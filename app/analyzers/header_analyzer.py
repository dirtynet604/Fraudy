class HeaderAnalyzer:

    def analyze(self, headers):

        findings = []

        spf = headers.get("Received-SPF")

        if spf and "fail" in spf.lower():
            findings.append("SPF Failed")

        dmarc = headers.get("Authentication-Results")

        if dmarc and "dmarc=fail" in dmarc.lower():
            findings.append("DMARC Failed")

        return findings
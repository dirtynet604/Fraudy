class AttachmentAnalyzer:

    HIGH_RISK_EXTENSIONS = [
        ".exe",
        ".scr",
        ".js",
        ".vbs",
        ".bat",
        ".iso"
    ]

    def analyze(self, attachments):

        findings = []

        for attachment in attachments:

            filename = attachment["filename"]

            for ext in self.HIGH_RISK_EXTENSIONS:

                if filename.endswith(ext):
                    findings.append(
                        f"Dangerous attachment {filename}"
                    )

        return findings
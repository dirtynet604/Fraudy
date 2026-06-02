from parsers.email_parser import EmailParser
from analyzers.header_analyzer import HeaderAnalyzer
from analyzers.url_analyzer import URLAnalyzer
from analyzers.attachment_analyzer import AttachmentAnalyzer
from analyzers.semantic_analyzer import SemanticAnalyzer
from scoring.risk_engine import RiskEngine

def run(email_file):

    parser = EmailParser()

    email = parser.parse(email_file)

    header_findings = HeaderAnalyzer().analyze(email)

    urls = []

    url_findings = URLAnalyzer().analyze(urls)

    attachments = []

    attachment_findings = (
        AttachmentAnalyzer().analyze(attachments)
    )

    semantic_findings = (
        SemanticAnalyzer().analyze(email)
    )

    score = RiskEngine().calculate(
        header_findings,
        url_findings,
        attachment_findings,
        semantic_findings
    )

    print(score)

if __name__ == "__main__":
    run("sample.eml")
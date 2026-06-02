from email import policy
from email.parser import BytesParser

class EmailParser:

    def parse(self, file_path):

        with open(file_path, "rb") as fp:
            msg = BytesParser(policy=policy.default).parse(fp)

        return msg
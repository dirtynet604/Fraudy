from pydantic import BaseModel

class EmailData(BaseModel):
    headers: dict
    body: str
    urls: list[str]
    attachments: list[dict]
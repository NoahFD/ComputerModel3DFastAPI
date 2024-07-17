from pydantic import BaseModel


class MessagePrompt(BaseModel):
    prompt: str

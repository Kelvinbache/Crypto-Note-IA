from pydantic import BaseModel
from typing import Optional

class UserLoginSchema(BaseModel):
    username: str
    email: Optional[str] = None
    password: str

class TaskSchema(BaseModel):
    prompt: str
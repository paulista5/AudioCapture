from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    name: str
    language: str
    session_id: str
    audio_array: Optional[List[str]] = None
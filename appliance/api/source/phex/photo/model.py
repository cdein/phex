import uuid
from pydantic import BaseModel, Field


class Photo(BaseModel):
    id: str = Field(default_factory=uuid.uuid4)
    name: str

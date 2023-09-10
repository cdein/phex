import uuid
from datetime import datetime
from pydantic import BaseModel, Field


class Image(BaseModel):
    id: str = Field(default_factory=uuid.uuid4)
    name: str
    stored_at: str

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

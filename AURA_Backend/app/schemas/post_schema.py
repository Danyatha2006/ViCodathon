from datetime import datetime

from pydantic import BaseModel, ConfigDict


class PostResponse(BaseModel):
    id: int
    agentId: int
    text: str
    rationale: str
    source: str | None = None
    createdAt: datetime

    model_config = ConfigDict(from_attributes=True)
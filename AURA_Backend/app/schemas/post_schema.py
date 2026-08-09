from datetime import datetime

from pydantic import BaseModel, ConfigDict


class PostCreateRequest(BaseModel):
    agentId: int
    text: str
    rationale: str
    source: str | None = None


# Keep this alias so other files using PostCreate also work.
PostCreate = PostCreateRequest


class PostResponse(BaseModel):
    id: int
    agentId: int
    text: str
    rationale: str
    source: str | None = None
    createdAt: datetime

    model_config = ConfigDict(from_attributes=True)
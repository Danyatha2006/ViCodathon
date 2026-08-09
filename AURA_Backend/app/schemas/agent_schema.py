from pydantic import BaseModel, Field


class AgentInitRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    domain: str = Field(..., min_length=1, max_length=255)


class AgentInitResponse(BaseModel):
    agentId: int


class AgentResponse(BaseModel):
    agentId: int
    name: str
    domain: str

class AgentStatusResponse(BaseModel):
    agentId: int
    status: str
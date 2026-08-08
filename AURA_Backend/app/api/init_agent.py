from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.agent_schema import AgentInitRequest, AgentInitResponse
from app.services.agent_service import initialize_agent


router = APIRouter(
    prefix="/api/agent",
    tags=["Agent"],
)


@router.post("/init", response_model=AgentInitResponse)
def init_agent(
    request: AgentInitRequest,
    db: Session = Depends(get_db),
):
    agent = initialize_agent(
        db=db,
        name=request.name,
        domain=request.domain,
    )

    return AgentInitResponse(agentId=agent.id)
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.crud import get_agent
from app.database.database import get_db
from app.schemas.agent_schema import (
    AgentInitRequest,
    AgentInitResponse,
    AgentResponse,
    AgentStatusResponse,
)
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


@router.get("/{agent_id}", response_model=AgentResponse)
def get_agent_details(
    agent_id: int,
    db: Session = Depends(get_db),
):
    agent = get_agent(db, agent_id)

    if agent is None:
        raise HTTPException(
            status_code=404,
            detail="Agent not found",
        )

    return AgentResponse(
        agentId=agent.id,
        name=agent.name,
        domain=agent.domain,
    )


@router.get("/{agent_id}/status", response_model=AgentStatusResponse)
def get_agent_status(
    agent_id: int,
    db: Session = Depends(get_db),
):
    agent = get_agent(db, agent_id)

    if agent is None:
        raise HTTPException(
            status_code=404,
            detail="Agent not found",
        )

    return AgentStatusResponse(
        agentId=agent.id,
        status="ready",
    )
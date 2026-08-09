from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.crud import get_agent
from app.database.database import get_db
from app.schemas.post_schema import PostCreate, PostResponse
from app.services.post_service import publish_post

router = APIRouter(
    prefix="/api/agent",
    tags=["Posts"],
)


@router.post("/posts", response_model=PostResponse)
def create_agent_post(
    request: PostCreate,
    db: Session = Depends(get_db),
):
    agent = get_agent(db, request.agentId)

    if agent is None:
        raise HTTPException(
            status_code=404,
            detail="Agent not found",
        )

    post = publish_post(
        db=db,
        agent_id=request.agentId,
        text=request.text,
        rationale=request.rationale,
        source=request.source,
    )

    return PostResponse(
        id=post.id,
        agentId=post.agent_id,
        text=post.text,
        rationale=post.rationale,
        source=post.source,
        createdAt=post.created_at,
    )
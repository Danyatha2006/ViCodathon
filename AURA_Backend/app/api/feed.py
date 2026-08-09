from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database.crud import get_agent
from app.database.database import get_db
from app.schemas.post_schema import PostResponse
from app.services.post_service import get_agent_feed


router = APIRouter(
    prefix="/api/agent",
    tags=["Feed"],
)


@router.get("/feed", response_model=list[PostResponse])
def get_feed(
    agentId: int = Query(..., gt=0),
    db: Session = Depends(get_db),
):
    agent = get_agent(db, agentId)

    if agent is None:
        raise HTTPException(
            status_code=404,
            detail="Agent not found",
        )

    posts = get_agent_feed(
        db=db,
        agent_id=agentId,
    )

    return [
        PostResponse(
            id=post.id,
            agentId=post.agent_id,
            text=post.text,
            rationale=post.rationale,
            source=post.source,
            createdAt=post.created_at,
        )
        for post in posts
    ]
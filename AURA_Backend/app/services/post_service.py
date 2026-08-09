from sqlalchemy.orm import Session

from app.database.crud import create_post, get_posts
from app.database.models import Post


def publish_post(
    db: Session,
    agent_id: int,
    text: str,
    rationale: str,
    source: str | None = None,
) -> Post:
    """Store a generated post for an agent."""
    return create_post(
        db=db,
        agent_id=agent_id,
        text=text,
        rationale=rationale,
        source=source,
    )


def get_agent_feed(
    db: Session,
    agent_id: int,
    limit: int = 50,
) -> list[Post]:
    """Retrieve an agent's feed, newest posts first."""
    return get_posts(
        db=db,
        agent_id=agent_id,
        limit=limit,
    )
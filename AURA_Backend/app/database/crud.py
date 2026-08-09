from sqlalchemy.orm import Session

from app.database.models import Agent, Post


def create_agent(db: Session, name: str, domain: str) -> Agent:
    """Create and persist a new agent."""
    agent = Agent(
        name=name,
        domain=domain,
    )

    db.add(agent)
    db.commit()
    db.refresh(agent)

    return agent


def get_agent(db: Session, agent_id: int) -> Agent | None:
    """Retrieve an agent by ID."""
    return db.query(Agent).filter(Agent.id == agent_id).first()


def create_post(
    db: Session,
    agent_id: int,
    text: str,
    rationale: str,
    source: str | None = None,
) -> Post:
    """Create and persist a post for an agent."""
    post = Post(
        agent_id=agent_id,
        text=text,
        rationale=rationale,
        source=source,
    )

    db.add(post)
    db.commit()
    db.refresh(post)

    return post


def get_posts(
    db: Session,
    agent_id: int,
    limit: int = 50,
) -> list[Post]:
    """Return an agent's posts, newest first."""
    return (
        db.query(Post)
        .filter(Post.agent_id == agent_id)
        .order_by(Post.created_at.desc())
        .limit(limit)
        .all()
    )
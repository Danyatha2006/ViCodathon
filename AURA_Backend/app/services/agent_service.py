from sqlalchemy.orm import Session

from app.database.crud import create_agent, get_agent
from app.database.models import Agent


def initialize_agent(
    db: Session,
    name: str,
    domain: str,
) -> Agent:
    """Create and persist an agent."""
    return create_agent(
        db=db,
        name=name,
        domain=domain,
    )


def get_agent_by_id(
    db: Session,
    agent_id: int,
) -> Agent | None:
    """Retrieve an agent by ID."""
    return get_agent(
        db=db,
        agent_id=agent_id,
    )
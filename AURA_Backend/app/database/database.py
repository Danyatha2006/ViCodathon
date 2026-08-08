from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# AURA_Backend/
# └── database/
#     └── aura.db
BASE_DIR = Path(__file__).resolve().parents[2]
DATABASE_DIR = BASE_DIR / "database"
DATABASE_DIR.mkdir(parents=True, exist_ok=True)

DATABASE_URL = f"sqlite:///{DATABASE_DIR / 'aura.db'}"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def get_db():
    """
    Provide a database session for API/service operations.

    The session is always closed after use.
    """
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
from fastapi import FastAPI

from app.api.feed import router as feed_router
from app.api.init_agent import router as agent_router
from app.database.database import engine
from app.database.models import Base


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AURA Backend API",
    description="Backend API for the AURA autonomous AI creator.",
    version="1.0.0",
)

app.include_router(agent_router)
app.include_router(feed_router)


@app.get("/")
def root():
    return {
        "status": "ok",
        "service": "AURA Backend",
    }

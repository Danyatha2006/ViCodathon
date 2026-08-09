from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.feed import router as feed_router
from app.api.init_agent import router as agent_router
from app.api.process import router as process_router
from app.api.posts import router as posts_router
from app.database.database import engine
from app.database.models import Base


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="AURA Backend API",
    description="Backend API for the AURA autonomous AI creator.",
    version="1.0.0",
)


# Allow the Vite frontend to communicate with the FastAPI backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# API routes
app.include_router(feed_router)
app.include_router(posts_router)
app.include_router(agent_router)
app.include_router(process_router)


@app.get("/")
def root():
    return {
        "status": "ok",
        "service": "AURA Backend",
    }

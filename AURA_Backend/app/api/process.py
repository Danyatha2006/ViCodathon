from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.ai_service import process_topic


router = APIRouter(
    prefix="/api/agent",
    tags=["AI"],
)


class ProcessTopicRequest(BaseModel):
    topic: str


@router.post("/process")
def process_agent_topic(request: ProcessTopicRequest):
    try:
        result = process_topic(request.topic)

        if result.get("status") == "ERROR":
            raise HTTPException(
                status_code=500,
                detail=result.get("reason", "AI processing failed"),
            )

        return result

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"AI processing failed: {exc}",
        )
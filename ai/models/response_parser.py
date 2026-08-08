from pydantic import BaseModel, Field


class TopicAnalysisResponse(BaseModel):
    topic: str = Field(
        description="The main AI or technology topic being analyzed."
    )

    summary: str = Field(
        description="A short summary of the topic."
    )

    relevance_score: int = Field(
        ge=0,
        le=100,
        description="How relevant the topic is to AURA's domain, from 0 to 100."
    )

    novelty_score: int = Field(
        ge=0,
        le=100,
        description="How new or non-repetitive the topic appears, from 0 to 100."
    )

    security_relevance_score: int = Field(
        ge=0,
        le=100,
        description="How relevant the topic is to AI security, from 0 to 100."
    )


class EditorialDecisionResponse(BaseModel):
    decision: str = Field(
        description="The publishing decision. Must be PUBLISH or REJECT."
    )

    reason: str = Field(
        description="Why the topic should be published or rejected."
    )


class GeneratedPostResponse(BaseModel):
    post: str = Field(
        description="The final social media post written in AURA's voice."
    )


class RationaleResponse(BaseModel):
    why_selected: str = Field(
        description="Why this topic was selected."
    )

    why_now: str = Field(
        description="Why this topic is relevant now."
    )

    source_summary: str = Field(
        description="Brief explanation of the information sources used."
    )
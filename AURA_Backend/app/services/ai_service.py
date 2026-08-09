import sys
from pathlib import Path
from typing import Any


# Add AI ENGINEER to Python path
PROJECT_ROOT = Path(__file__).resolve().parents[3]
AI_ENGINEER_PATH = PROJECT_ROOT / "AI ENGINEER"

if str(AI_ENGINEER_PATH) not in sys.path:
    sys.path.insert(0, str(AI_ENGINEER_PATH))

from integration.ai_brain_adapter import AIBrainAdapter


def process_topic(topic: str) -> dict[str, Any]:
    """Send a topic to the AURA AI Brain and return its result."""

    adapter = AIBrainAdapter()

    try:
        return adapter.process_topic(topic)
    finally:
        adapter.close()
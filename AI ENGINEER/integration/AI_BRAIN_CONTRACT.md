# AURA AI BRAIN — TEAM CONTRACT

## Input

The AI Brain accepts one topic string.

```python
result = brain.process_topic(topic)
```

## Output

The AI Brain returns a JSON-safe Python dictionary.

### Published Result

```json
{
  "status": "PUBLISHED",
  "reason": "APPROVED",
  "topic": "A new AI security development.",
  "overall_score": 94.45,
  "duplicate_check": {
    "is_duplicate": false,
    "recommendation": "PUBLISH_NEW_TOPIC"
  },
  "decision": {
    "decision": "PUBLISH",
    "reason": "Highly relevant AI security topic."
  },
  "generated_post": {
    "post": "Generated AURA post."
  },
  "rationale": {
    "why_selected": "Relevant AI security development.",
    "why_now": "Important current security concern.",
    "source_summary": "Based on supplied topic information."
  }
}
```

### Rejected Result

```json
{
  "status": "REJECTED",
  "reason": "EDITORIAL_DECISION"
}
```

### Duplicate Result

```json
{
  "status": "REJECTED",
  "reason": "DUPLICATE"
}
```

Rejected results do not contain:

* `generated_post`
* `rationale`

## Integration Entry Point

```python
from integration.ai_brain_adapter import AIBrainAdapter

brain = AIBrainAdapter()

result = brain.process_topic(topic)

brain.close()
```

## Integration Rule

The rest of the team should use `AIBrainAdapter` as the integration boundary.

Internal AI Brain components should not be accessed directly.

## AI Brain Status

The AI Brain implementation, testing, public API, adapter, and offline integration are complete.

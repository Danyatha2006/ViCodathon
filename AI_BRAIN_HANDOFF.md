# AURA AI BRAIN — HANDOFF DOCUMENT

## 1. Overview

The AURA AI Brain is the intelligence layer responsible for evaluating discovered topics, deciding whether they should be published, generating the final post and editorial rationale, and storing published content for future duplicate detection.

---

## 2. AI Brain Entry Points

### Public API

```python
from ai import AURAAI

ai = AURAAI()

result = ai.process(topic)

ai.close()
```

### Team Integration Adapter

```python
from integration.ai_brain_adapter import AIBrainAdapter

brain = AIBrainAdapter()

result = brain.process_topic(topic)

brain.close()
```

The team-facing integration should use `AIBrainAdapter`.

---

## 3. Input

The AI Brain accepts a topic as a string.

Example:

```python
topic = (
    "A new runtime monitoring technique detects "
    "suspicious behavior in autonomous AI agents."
)
```

Empty or whitespace-only topics are rejected.

---

## 4. AI Pipeline

```text
Discovered Topic
      ↓
Memory Search
      ↓
Topic Analysis
      ↓
Relevance Scoring
      ↓
Duplicate Detection
      ↓
Editorial Decision
      ↓
Content Generation
      ↓
Rationale Generation
      ↓
Memory Storage
      ↓
Final Result
```

---

## 5. Topic Analysis

The Topic Analyzer evaluates:

* Topic summary
* Relevance score
* Novelty score
* Security relevance score

The analysis is returned as a structured response.

Example:

```python
TopicAnalysisResponse(
    topic="...",
    summary="...",
    relevance_score=95,
    novelty_score=90,
    security_relevance_score=98,
)
```

---

## 6. Relevance Scoring

The Relevance Scorer calculates an overall score from the topic analysis.

The score is used by the editorial decision stage.

---

## 7. Duplicate Detection

The Duplicate Checker compares the topic against previous memory.

Possible outcomes include:

```text
PUBLISH_NEW_TOPIC
REJECT_DUPLICATE
```

If a topic is detected as a duplicate:

```text
Status = REJECTED
Reason = DUPLICATE
```

Content generation and rationale generation are skipped.

---

## 8. Editorial Decision

The Decision Engine determines whether the topic should be published.

Possible decision:

```text
PUBLISH
REJECT
```

If rejected:

```text
Status = REJECTED
Reason = EDITORIAL_DECISION
```

Content and rationale generation are skipped.

---

## 9. Content Generation

For an approved topic, the Content Generator creates the final AURA post.

The generated result is structured as:

```python
GeneratedPostResponse(
    post="..."
)
```

Content is generated only after:

1. Topic analysis
2. Scoring
3. Duplicate check
4. Editorial approval

---

## 10. Rationale Generation

For an approved topic, the Rationale Generator produces:

```python
RationaleResponse(
    why_selected="...",
    why_now="...",
    source_summary="..."
)
```

Rationale generation occurs after successful content generation.

---

## 11. Memory Storage

Only successfully processed and published content is saved to memory.

Failed content generation or rationale generation must not be stored.

Memory is used for future topic comparison and duplicate detection.

---

## 12. Result Contract

### Published Result

A successful result contains:

```text
status
reason
topic
analysis
overall_score
duplicate_check
decision
generated_post
rationale
```

Expected values:

```text
status = PUBLISHED
reason = APPROVED
decision.decision = PUBLISH
```

### Rejected Result

A rejected topic contains the decision information but does not contain:

```text
generated_post
rationale
```

Possible rejection reasons:

```text
EDITORIAL_DECISION
DUPLICATE
```

---

## 13. JSON-Safe Output

The public AURA interface converts structured AI responses into JSON-safe Python dictionaries.

Example:

```python
result = ai.process(topic)
```

The returned result can be passed to a web API or another application layer.

---

## 14. Error Handling

The AI Brain validates invalid input.

Example:

```text
Topic cannot be empty.
```

Generation failures are propagated and failed content is not stored in memory.

Rationale generation failures are also propagated and failed results are not stored.

---

## 15. Gemini / LLM Configuration

The LLM client reads the API key from:

```text
GEMINI_API_KEY
```

The key should be stored in `.env`.

Example:

```text
GEMINI_API_KEY=your_api_key_here
```

The `.env` file must not be committed to Git.

The current default Gemini model is configured in:

```text
ai/models/llm_client.py
```

---

## 16. Dependencies

Install project dependencies with:

```powershell
pip install -r requirements.txt
```

The project uses the Gemini Python SDK and Pydantic structured responses.

---

## 17. Testing

Offline tests use fake components and do not require Gemini API calls.

Important tests include:

```powershell
python -m tests.test_ai_engine_reject
python -m tests.test_ai_engine_duplicate
python -m tests.test_ai_engine_generation_failure
python -m tests.test_ai_engine_rationale_failure
python -m tests.test_ai_engine_result_contract_integration
python -m tests.test_final_ai_handoff
python -m tests.test_final_offline_integration
```

The final offline integration test verifies that the team-facing AI Brain interface works without consuming Gemini quota.

---

## 18. Gemini Quota Note

Live Gemini execution depends on the configured Gemini API quota.

If the API returns:

```text
429 RESOURCE_EXHAUSTED
```

the AI Brain code does not need to be modified.

Use the offline/fake-LLM tests for development and integration testing until the API quota becomes available again.

---

## 19. Team Integration

The preferred team-facing entry point is:

```python
from integration.ai_brain_adapter import AIBrainAdapter

brain = AIBrainAdapter()

result = brain.process_topic(topic)
```

The integration layer should treat the returned dictionary as the AI Brain result contract.

The AI Brain should not be accessed by directly modifying its internal components in production integration code.

---

## 20. AI Brain Responsibilities

The AI Brain owns:

* Persona behavior
* Topic analysis
* Relevance scoring
* Duplicate detection
* Editorial decisions
* AI post generation
* Editorial rationale generation
* Memory interaction
* Structured AI responses
* Failure handling
* Result serialization
* Team-facing AI interface

---

## 21. Current Completion Status

```text
AI Engine                  COMPLETE
Persona                    COMPLETE
Topic Analysis             COMPLETE
Relevance Scoring          COMPLETE
Duplicate Detection        COMPLETE
Editorial Decision         COMPLETE
Content Generation         COMPLETE
Rationale Generation       COMPLETE
Memory Integration         COMPLETE
Failure Handling           COMPLETE
Result Contract            COMPLETE
Public API                 COMPLETE
Integration Adapter        COMPLETE
Offline Integration        COMPLETE
Final Handoff Test         COMPLETE
```

The AI Brain is ready for final team integration.

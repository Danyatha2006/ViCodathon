import os
import sys
import requests

from AUTOMATION.discovery.news_fetcher import fetch_latest_news


# Allow importing the AI Engineer package

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

AI_ENGINEER_PATH = os.path.join(
    PROJECT_ROOT,
    "AI ENGINEER",
)

if AI_ENGINEER_PATH not in sys.path:
    sys.path.insert(0, AI_ENGINEER_PATH)

from integration.ai_brain_adapter import AIBrainAdapter


BACKEND_URL = "http://127.0.0.1:8000"
AGENT_ID = 1

def publish_to_backend(
    text: str,
    rationale: str,
    source: str | None = None,
):
    """Publish an approved AURA post to the backend."""

    response = requests.post(
        f"{BACKEND_URL}/api/agent/posts",
        json={
            "agentId": AGENT_ID,
            "text": text,
            "rationale": rationale,
            "source": source,
        },
        timeout=10,
    )

    response.raise_for_status()

    return response.json()


def run_agent():
    """
    Run the complete AURA autonomous workflow.

    News
      ↓
    AI Brain
      ↓
    Editorial Decision
      ↓
    Backend
    """

    print("\n===== AURA AUTONOMOUS AGENT =====")
    print("Starting autonomous workflow...")

    articles = fetch_latest_news()

    print(f"Articles discovered: {len(articles)}")

    if not articles:
        print("No new articles found.")
        return []

    brain = AIBrainAdapter()

    published = []
    rejected = []
    failed = []

    try:
        for article in articles:

            title = article.get("title", "").strip()
            summary = article.get("summary", "").strip()
            source = article.get("url", "").strip()

            if not title:
                failed.append({
                    "title": "Unknown article",
                    "reason": "Missing title",
                })
                continue

            topic = title

            if summary:
                topic = f"{title}\n\n{summary}"

            print(f"\nProcessing: {title}")

            try:
                # -----------------------------------------
                # AI ANALYSIS + EDITORIAL DECISION
                # -----------------------------------------

                result = brain.process_topic(topic)

                status = str(
                    result.get("status", "")
                ).strip().upper()

                print(f"AI decision: {status}")

                # -----------------------------------------
                # REJECTED
                # -----------------------------------------

                if status != "PUBLISHED":

                    rejected.append({
                        "title": title,
                        "reason": result.get(
                            "rationale",
                            "AI rejected the topic.",
                        ),
                    })

                    print("→ Not published.")
                    continue

                # -----------------------------------------
                # GET GENERATED POST
                # -----------------------------------------

                generated_post = result.get(
                    "generated_post"
                )

                rationale = result.get(
                    "rationale"
                )

                if isinstance(generated_post, dict):

                    post_text = generated_post.get(
                        "post",
                        "",
                    )

                else:

                    post_text = getattr(
                        generated_post,
                        "post",
                        "",
                    )

                if isinstance(rationale, dict):

                    rationale_text = rationale.get(
                        "why_selected",
                        "",
                    )

                else:

                    rationale_text = getattr(
                        rationale,
                        "why_selected",
                        "",
                    )

                if not post_text:

                    failed.append({
                        "title": title,
                        "reason": "AI generated no post.",
                    })

                    print(
                        "→ No generated post. "
                        "Article failed."
                    )

                    continue

                print("→ AI generated a post.")

                # -----------------------------------------
                # BACKEND PUBLISHING
                # -----------------------------------------

                try:

                    published_post = publish_to_backend(
                        text=post_text,
                        rationale=rationale_text,
                        source=source,
                    )

                    published.append({
                        "title": title,
                        "post": published_post,
                    })

                    print(
                        "→ Published to backend successfully."
                    )

                except Exception as backend_error:

                    # IMPORTANT:
                    # The AI already decided PUBLISHED.
                    # Backend failure is tracked separately
                    # instead of hiding the AI result.

                    failed.append({
                        "title": title,
                        "reason": (
                            "Backend publishing failed: "
                            f"{backend_error}"
                        ),
                    })

                    print(
                        "→ AI approved the article, "
                        "but backend publishing failed."
                    )

            except Exception as exc:

                failed.append({
                    "title": title,
                    "reason": str(exc),
                })

                print(
                    f"→ Error processing article: {exc}"
                )

    finally:
        brain.close()

    # ---------------------------------------------
    # FINAL SUMMARY
    # ---------------------------------------------

    print("\n===== WORKFLOW COMPLETE =====")

    print(
        f"Articles discovered: {len(articles)}"
    )

    print(
        f"Posts published successfully: "
        f"{len(published)}"
    )

    print(
        f"Articles rejected: "
        f"{len(rejected)}"
    )

    print(
        f"Articles failed: "
        f"{len(failed)}"
    )

    print(
        f"Total processed: "
        f"{len(published) + len(rejected) + len(failed)}"
    )

    # ---------------------------------------------
    # FAILED ARTICLES
    # ---------------------------------------------

    if failed:

        print("\n===== FAILED ARTICLES =====")

        for item in failed:

            print(
                f"• {item['title']}"
            )

            print(
                f"  Reason: {item['reason']}"
            )

    return published


if __name__ == "__main__":
    run_agent()
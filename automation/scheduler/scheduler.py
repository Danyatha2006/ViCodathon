from apscheduler.schedulers.blocking import BlockingScheduler
from automation.agent.agent_loop import run_agent


def run_autonomous_agent():
    print("\n===== AUTOMATIC AURA AGENT =====")

    articles = run_agent()

    print(f"Automatic run completed.")
    print(f"New articles collected: {len(articles)}")


def start_scheduler():
    scheduler = BlockingScheduler()

    # Run every 10 minutes
    scheduler.add_job(
        run_autonomous_agent,
        "interval",
        minutes=10
    )

    print("Scheduler started.")
    print("Autonomous agent will run every 10 minutes.")

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        print("Scheduler stopped.")


if __name__ == "__main__":
    start_scheduler()
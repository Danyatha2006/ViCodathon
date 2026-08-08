from apscheduler.schedulers.blocking import BlockingScheduler
from automation.discovery.news_fetcher import fetch_latest_news


def run_news_collection():
    print("\n===== AUTOMATIC NEWS COLLECTION =====")

    articles = fetch_latest_news()

    print(f"New articles collected: {len(articles)}")


def start_scheduler():
    scheduler = BlockingScheduler()

    # Run every 10 minutes
    scheduler.add_job(
        run_news_collection,
        "interval",
        minutes=10
    )

    print("Scheduler started.")
    print("News collection will run every 10 minutes.")

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        print("Scheduler stopped.")


if __name__ == "__main__":
    start_scheduler()
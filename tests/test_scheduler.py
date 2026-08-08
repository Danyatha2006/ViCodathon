from automation.scheduler.scheduler import run_autonomous_agent


def test_scheduler_function_runs():
    result = run_autonomous_agent()

    assert result is None

from AUTOMATION.agent.agent_loop import run_agent


def test_autonomous_agent_returns_list():
    articles = run_agent()

    assert isinstance(articles, list)

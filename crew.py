from crewai import Agent, Task, Crew, Process
from tools.custom_tool import search_tool
import yaml
from pathlib import Path

def load_yaml(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def build_agents():
    config = load_yaml("config/agents.yaml")
    agents = {}
    for name, data in config.items():
        tools = [search_tool] if "serper_tool" in data.get("tools", []) else []
        agents[name] = Agent(
            role=data["role"],
            goal=data["goal"],
            backstory=data["backstory"],
            tools=tools,
            verbose=True,
            memory=True
        )
    return agents

def build_tasks(agents, url):
    config = load_yaml("config/tasks.yaml")
    tasks = []

    claims_placeholder = "{claims}"

    extract_task = Task(
        description=config["extract_claims"]["description"].format(url=url),
        expected_output=config["extract_claims"]["expected_output"],
        agent=agents["extractor"]
    )

    fact_task = Task(
        description=config["fact_check_claims"]["description"].replace("{claims}", "<<extract_claims>>"),
        expected_output=config["fact_check_claims"]["expected_output"],
        agent=agents["fact_checker"]
    )

    summary_task = Task(
        description=config["write_summary"]["description"].replace("{claims}", "<<fact_check_claims>>"),
        expected_output=config["write_summary"]["expected_output"],
        agent=agents["summary_writer"]
    )

    return [extract_task, fact_task, summary_task]

def get_url_crew(url):
    agents = build_agents()
    tasks = build_tasks(agents, url)
    return Crew(
        agents=list(agents.values()),
        tasks=tasks,
        process=Process.sequential
    )

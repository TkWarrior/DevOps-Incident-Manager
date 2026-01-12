from typing_extensions import TypedDict
from agent.github_agent import broken_method

class IncidentState(TypedDict):
    logs: str
    error_summary: str
    broken_method: str
    root_cause: str
    fix: str
    patch: str
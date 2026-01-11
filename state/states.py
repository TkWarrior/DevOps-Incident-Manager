from typing_extensions import TypedDict

class IncidentState(TypedDict):
    logs: str
    error_summary: str
    root_cause: str
    fix: str

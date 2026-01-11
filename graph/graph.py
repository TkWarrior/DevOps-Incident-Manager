from langgraph.graph import StateGraph
from state.states import IncidentState
from agent.agents import log_reader_agent, root_cause_agent, fix_agent

graph = StateGraph(IncidentState)

graph.add_node("log_reader", log_reader_agent)
graph.add_node("root_cause", root_cause_agent)
graph.add_node("fix", fix_agent)

graph.set_entry_point("log_reader")
graph.add_edge("log_reader", "root_cause")
graph.add_edge("root_cause", "fix")

agent = graph.compile()

from langgraph.graph import StateGraph, START, END
from state.states import IncidentState
from agent.agents import log_reader_agent, root_cause_agent, fix_agent , patch_agent

graph = StateGraph(IncidentState)

graph.add_node("log_reader_agent", log_reader_agent)
graph.add_node("root_cause_agent", root_cause_agent)
graph.add_node("fix_agent", fix_agent)
graph.add_node("patch_agent", patch_agent)

graph.set_entry_point("log_reader_agent") ## Starting point of the graph

graph.add_edge("log_reader_agent", "root_cause_agent")
graph.add_edge("root_cause_agent", "fix_agent")
graph.add_edge("fix_agent", "patch_agent")
graph.add_edge("patch_agent", END)

agent = graph.compile()
print(agent)

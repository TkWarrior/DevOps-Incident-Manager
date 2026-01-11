from llm import ask
from log_reader.log_reader import fetch_logs, has_error
from agent.agents import log_reader
from state.states import IncidentState


if __name__ == "__main__":
    
    logs = fetch_logs()
    state = {"logs": logs}
    
    print("state" ,state) 
    print(log_reader(state))
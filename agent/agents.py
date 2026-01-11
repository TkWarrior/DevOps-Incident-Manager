from llm import ask

# Agent for log readin and adding error summary to the state
def log_reader_agent(state):
    prompt = f"""
    Extract the main error from these logs:

    {state['logs']}
    """
    return {"error_summary": ask(prompt)}

# Agent for root cause analysis and adding root cause to the state
def root_cause_agent(state):
    prompt = f"""
    Error:
    {state['error_summary']}

    Explain the most likely root cause in simple terms.
    """
    return {"root_cause": ask(prompt)}

# Agent for suggesting code fix and adding fix to the state
def fix_agent(state):
    prompt = f"""
    Root cause:
    {state['root_cause']}

    Suggest a safe code fix in simple terms.
    """
    return {"fix": ask(prompt)}



from llm import ask

def log_reader_agent(state):
    prompt = f"""
    Extract the main error from these logs:

    {state['logs']}
    """
    return {"error_summary": ask(prompt)}

def root_cause_agent(state):
    prompt = f"""
    Error:
    {state['error_summary']}

    Explain the most likely root cause in simple terms.
    """
    return {"root_cause": ask(prompt)}

def fix_agent(state):
    prompt = f"""
    Root cause:
    {state['root_cause']}

    Suggest a safe code fix in simple terms.
    """
    return {"fix": ask(prompt)}

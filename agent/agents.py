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

# Agent for generating code patch and adding patch to the state
def patch_agent(state):
    prompt = f"""
    You are an autonomous code-fixing agent.

    This is the exact function that caused a runtime error:
    <FUNCTION>
    {state["broken_method"]}
    </FUNCTION>

    Root cause:
    {state["root_cause"]}

    Rules:
    - Return the SAME function signature
    - Do NOT change routes, annotations, decorators, or names
    - Modify ONLY the function body
    - The function must NEVER throw the same runtime exception again
    - Do NOT add comments
    - Do NOT add explanations
    - Do NOT output multiple options
    - Output ONLY the corrected function

    Return the fixed function now:
    """
    return {"patch": ask(prompt)}

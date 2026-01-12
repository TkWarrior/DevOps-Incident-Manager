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
    You are an autonomous software engineer fixing a production bug.

    This function caused a runtime error:

    <FUNCTION>
    {state['broken_method']}
    </FUNCTION>

    Root cause:
    {state['root_cause']}

    Rules:
    - You MUST return the SAME function (same name, parameters, routes, decorators, framework)
    - Modify ONLY the function body to fix the bug
    - Do NOT change imports, file structure, or surrounding code
    - Do NOT invent new classes, types, or return values
    - Do NOT add explanations or comments
    - Output ONLY valid code

    Return the corrected function:
    """
    return {"patch": ask(prompt)}

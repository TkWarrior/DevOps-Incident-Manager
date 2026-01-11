from log_reader.log_reader import fetch_logs
from graph.graph import agent

if __name__ == "__main__":
    
    logs = fetch_logs()

    result = agent.invoke({
        "logs": logs
    })

    print("\n🧠 ERROR:", result["error_summary"])
    print("\n🔍 ROOT CAUSE:", result["root_cause"])
    print("\n🛠 FIX:", result["fix"])
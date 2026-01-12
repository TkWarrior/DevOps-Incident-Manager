from log_reader.log_reader import fetch_logs
from graph.graph import agent
from agent.github_agent import create_pr

setverbose = True
setdebug = True

if __name__ == "__main__":
    
    logs = fetch_logs()

    result = agent.invoke({
        "logs": logs
    })

    print("\n🧠 ERROR:", result["error_summary"])
    print("\n🔍 ROOT CAUSE:", result["root_cause"])
    print("\n🛠 FIX:", result["fix"])
    print("\n� PATCH:\n", result["patch"])
    
    repo_name = "TkWarrior/crash_simulator"
    file_path = "src/main/java/com/example/demo/controller/CrashController.java"
    patch_code = result["patch"]
    
    pull_request_url = create_pr(repo_name , file_path , logs ,patch_code)
    
    print("pull request created at:", pull_request_url)
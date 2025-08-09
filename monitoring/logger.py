import os
import json
from datetime import datetime

def log_user_action(user_id, action, details):
    log_path = "monitoring/user_logs.json"
    log_dir = os.path.dirname(log_path)

    # 🛠️ Create folder if missing
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # 📝 Create file if missing
    if not os.path.exists(log_path):
        with open(log_path, "w") as f:
            json.dump([], f)

    # 📥 Load existing logs
    with open(log_path, "r") as f:
        logs = json.load(f)

    # ➕ Add new log
    logs.append({
        "user_id": user_id,
        "action": action,
        "timestamp": datetime.now().isoformat(),
        "details": details
    })

    # 💾 Save updated logs
    with open(log_path, "w") as f:
        json.dump(logs, f, indent=2)

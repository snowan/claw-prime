import json
import os
from datetime import datetime

STATE_FILE = "/Users/xiaowei.wan/clawd/memory/mission-control.json"

def get_status():
    if not os.path.exists(STATE_FILE):
        return {"revenue": 0, "target": 10000, "efficiency": 1.0, "last_nodes": []}
    with open(STATE_FILE, 'r') as f:
        return json.load(f)

def update_status(nodes, efficiency):
    status = get_status()
    status["last_nodes"] = nodes
    status["efficiency"] = efficiency
    status["last_update"] = datetime.now().isoformat()
    with open(STATE_FILE, 'w') as f:
        json.dump(status, f, indent=2)

def report():
    s = get_status()
    print(f"🛰️ MISSION CONTROL STATUS")
    print(f"--------------------------")
    print(f"Goal: ${s['revenue']} / ${s['target']}")
    print(f"Efficiency: {s['efficiency']*100:.1f}%")
    print(f"Active Context: {', '.join(s['last_nodes'])}")
    print(f"Update: {s.get('last_update', 'N/A')}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--report":
        report()

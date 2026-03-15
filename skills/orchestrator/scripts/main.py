import json
import sys

GRAPH_PATH = "/Users/xiaowei.wan/clawd/memory/skill-graph.json"
TELEMETRY_PATH = "/Users/xiaowei.wan/clawd/memory/mission-control.json"

def load_graph():
    with open(GRAPH_PATH, 'r') as f:
        return json.load(f)

def run_pipeline(name, input_val, target=None):
    graph = load_graph()
    if name not in graph['pipelines']:
        print(f"Error: Pipeline {name} not found.")
        return

    pipeline = graph['pipelines'][name]
    nodes = pipeline['nodes']
    
    print(f"🚀 Initializing Pipeline: {name}")
    print(f"📍 Goal: {pipeline['goal']}")
    print(f"🔗 Chain: {' -> '.join(nodes)}")
    
    # In a real execution, this would trigger sessions_spawn or exec
    # For the prototype, we log the intent to the orchestrator log
    log_action(name, input_val, nodes)

def log_action(pipeline, input_val, nodes):
    return {
        "pipeline": pipeline,
        "input": input_val,
        "nodes": nodes,
        "status": "initialized"
    }
    print("✅ Workflow graph validated. Ready for execution.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: orchestrator.py <pipeline_name> <input_value>")
    else:
        run_pipeline(sys.argv[1], sys.argv[2])

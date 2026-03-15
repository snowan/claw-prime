import json
import tempfile
import pytest
from unittest.mock import patch
from scripts.main import load_graph, run_pipeline

@pytest.fixture
def mock_graph(monkeypatch):
    graph_data = {
        "pipelines": {
            "test_pipe": {
                "goal": "generate $10k",
                "nodes": ["step1", "step2"]
            }
        }
    }
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        json.dump(graph_data, f)
        temp_path = f.name
    
    monkeypatch.setattr("scripts.main.GRAPH_PATH", temp_path)
    return temp_path

def test_load_graph(mock_graph):
    graph = load_graph()
    assert "test_pipe" in graph["pipelines"]

@patch("scripts.main.print")
def test_run_pipeline_success(mock_print, mock_graph):
    run_pipeline("test_pipe", "input_data")
    mock_print.assert_any_call("🚀 Initializing Pipeline: test_pipe")

@patch("scripts.main.print")
def test_run_pipeline_error(mock_print, mock_graph):
    run_pipeline("missing_pipe", "data")
    mock_print.assert_called_with("Error: Pipeline missing_pipe not found.")

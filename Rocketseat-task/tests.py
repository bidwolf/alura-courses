import requests
from models.task import Task

BASE_URL = "http://localhost:4444"
tasks: list[Task] = []


def test_create_task():
    new_task_data = {
        "title": "title for test suite",
        "description": "this is a test using pytest",
    }
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data, timeout=5000)
    response_json = response.json()
    assert response.status_code == 201
    assert "task" in response_json
    assert "createdAt" in response_json
    assert "id" in response_json["task"]
    assert "title" in response_json["task"]
    assert "description" in response_json["task"]
    assert "completed" in response_json["task"]
    assert not response_json["task"]["completed"]

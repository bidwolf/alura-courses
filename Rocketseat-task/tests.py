import requests
from models.task import Task

BASE_URL = "http://localhost:4444"
tasks: list[Task] = []


def test_create_task():
    """Ensures that a created task should return a json accordingly the schema below
    - task (the task created containing id, description, title and completed properties)
    - createdAt (datetime when the task has been created)
    """
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
    tasks.append(response_json["task"]["id"])


def test_get_task_list():
    """
    Ensures that the task list should return a json accordingly the schema below
    - tasks (the task list)
    - limit (the limit of tasks that will be returned)
    - offset (A quantity of tasks that will be ignored to pagination feature)
    """
    params = {"limit": 20, "offset": 0}
    response = requests.get(f"{BASE_URL}/tasks", timeout=5000, params=params)
    response_json = response.json()
    assert response.status_code == 200
    assert "limit" in response_json
    assert "total" in response_json
    assert "tasks" in response_json
    assert len(response_json["tasks"]) <= params["limit"]
    assert len(response_json["tasks"]) <= response_json["total"]


def test_get_task_by_id():
    """
    Ensures that the task with the given id is correctly returned
    """
    if tasks and len(tasks) > 0:
        task_id = tasks[0]
        response = requests.get(f"{BASE_URL}/tasks/{task_id}", timeout=5000)
        response_json = response.json()
        assert response.status_code == 200
        assert "id" in response_json
        assert "title" in response_json
        assert "description" in response_json
        assert "completed" in response_json

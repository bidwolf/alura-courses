"""This is the main module for the task API"""

import json
import datetime
from flask import Flask, request, Response
from models.task import Task

app = Flask(__name__)
tasks: list[Task] = []
task_id_control = 1


@app.route("/tasks", methods=["POST"])
def create():
    """Endpoint for create a new task"""
    global task_id_control
    payload = request.get_json()
    if not payload:
        return Response(
            status=400, response={"message": "You must send a title and a description"}
        )
    task_title = payload.get("title")
    task_description = payload.get("description")
    created_at = datetime.datetime.now().isoformat()
    if not task_title or not task_description:
        return Response(
            status=400, response={"message": "You must send a title and a description"}
        )
    new_task = Task(
        title=task_title, description=task_description, user_id=task_id_control
    )
    tasks.append(new_task)
    response = {"createdAt": created_at, "task": new_task.to_dict()}
    task_id_control += 1
    return Response(
        status=200, response=json.dumps(response), content_type="Application/JSON"
    )


@app.route("/tasks", methods=["GET"])
def list_all_tasks():
    INITIAL_TASK_LIMIT = 50
    task_limit = limit = request.args.get("limit")
    task_offset = offset = request.args.get("offset")
    total = len(tasks)

    if task_limit and task_limit.isdigit():
        limit = int(task_limit) if int(task_limit) > 0 else INITIAL_TASK_LIMIT
        task_limit = min(limit, total)
    else:
        task_limit = total if total < INITIAL_TASK_LIMIT else INITIAL_TASK_LIMIT
        limit = INITIAL_TASK_LIMIT
    if task_offset and task_offset.isdigit():
        offset = int(task_offset)
        task_offset = min(int(task_offset), total)
        if isinstance(task_limit, int) and task_limit > 0:
            task_limit = min(task_limit + offset, total)
    else:
        task_offset = 0
    current_tasks = list(map(lambda task: task.to_dict(), tasks))[
        task_offset:task_limit
    ]  # make a list of dict for each task starting from offset to limit
    response = {
        "limit": limit if isinstance(limit, int) else 0,
        "offset": offset if isinstance(offset, int) else 0,
        "total": total,
        "tasks": current_tasks,
    }
    return Response(
        status=200, response=json.dumps(response), content_type="Application/JSON"
    )


if __name__ == "__main__":
    app.run(debug=True, port=4444)

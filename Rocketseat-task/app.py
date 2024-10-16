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
        status=201, response=json.dumps(response), content_type="Application/JSON"
    )


@app.route("/tasks", methods=["GET"])
def list_all_tasks():
    default_task_limit = 50
    task_limit = limit = request.args.get("limit")
    task_offset = offset = request.args.get("offset")
    total = len(tasks)

    if task_limit and task_limit.isdigit():
        limit = int(task_limit) if int(task_limit) > 0 else default_task_limit
        task_limit = min(limit, total)
    else:
        task_limit = total if total < default_task_limit else default_task_limit
        limit = default_task_limit
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


@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task_by_id(task_id: int):
    """Get the specified task"""
    task = None
    for t in tasks:
        if t.id == task_id:
            task = t
            return Response(
                status=200,
                content_type="Application/JSON",
                response=json.dumps(task.to_dict()),
            )
    return Response(
        status=404,
        content_type="Application/JSON",
        response=json.dumps({"message": "Cannot find task."}),
    )


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id: int):
    """Update the task with the given id"""
    if not task_id:
        return Response(
            status=400,
            content_type="Application/JSON",
            response=json.dumps({"message": "Task id is required for this request."}),
        )
    if not isinstance(task_id, int):
        return Response(
            status=400,
            content_type="Application/JSON",
            response=json.dumps({"message": "Task id must be integer"}),
        )
    for task in tasks:
        if task.id == task_id:
            data = request.get_json()
            task.title = data["title"]
            task.description = data["description"]
            task.completed = data["completed"]
            updated_at = datetime.datetime.now().isoformat()
            return Response(
                status=200,
                content_type="Application/JSON",
                response=json.dumps({"updatedAt": updated_at, "task": task.to_dict()}),
            )
    return Response(
        status=404,
        content_type="Application/JSON",
        response=json.dumps({"message": "Cannot find any task with this id"}),
    )


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id: int):
    """Delete the task with the given id"""
    if not task_id:
        return Response(
            status=400,
            content_type="Application/JSON",
            response=json.dumps({"message": "Task id is required for this request."}),
        )
    if not isinstance(task_id, int):
        return Response(
            status=400,
            content_type="Application/JSON",
            response=json.dumps({"message": "Task id must be integer"}),
        )
    deleted_task = None
    for task in tasks:
        if task.id == task_id:
            deleted_task = task
            break
    deleted_at = datetime.datetime.now().isoformat()
    if not deleted_task:
        return Response(
            status=404,
            content_type="Application/JSON",
            response=json.dumps({"message": "Invalid task id"}),
        )
    tasks.remove(deleted_task)
    return Response(
        status=200,
        content_type="Application/JSON",
        response=json.dumps({"deletedAt": deleted_at, "task": deleted_task.to_dict()}),
    )


if __name__ == "__main__":
    app.run(debug=True, port=4444)

"""This is the main module for the task API"""

import json
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
    if not task_title or not task_description:
        return Response(
            status=400, response={"message": "You must send a title and a description"}
        )
    new_task = Task(
        title=task_title, description=task_description, user_id=task_id_control
    )
    tasks.append(new_task)
    response = new_task.to_dict()
    task_id_control += 1
    return Response(
        status=200, response=json.dumps(response), content_type="Application/JSON"
    )


if __name__ == "__main__":
    app.run(debug=True, port=4444)

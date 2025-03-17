import time

from flask import Flask, jsonify, abort, request,redirect,render_template,url_for

app=Flask(__name__)

tasks = [
    {"id": 1, "title": "Task One", "description": "Description for Task One", "done": False},
    {"id": 2, "title": "Task Two", "description": "Description for Task Two", "done": True},
    {"id": 3, "title": "Task Three", "description": "Description for Task Three", "done": False}
    ]
def gettask(task_id):
    return next((task for task in tasks if task["id"]==task_id),None)

@app.route('/tasks/<int:task_id>',methods=["DELETE"])
def delete_task_id(task_id):
    task=gettask(task_id)
    if task is None:
        abort(404)
    tasks.remove(task)
    return jsonify({"tasks":tasks}),200


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description", "")
        if not title:
            abort(400)
        new_task = {
            "id": tasks[-1]["id"] + 1 if tasks else 1,
            "title": title,
            "description": description,
            "done": False
        }
        tasks.append(new_task)
        return redirect(url_for("index"))
    return render_template("index.html", tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)

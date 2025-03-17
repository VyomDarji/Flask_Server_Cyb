from flask import Flask, jsonify, abort, request, redirect, render_template, url_for

app = Flask(__name__)

# Sample task list
tasks = [
    {"id": 1, "title": "Buy groceries", "description": "Milk, Bread, Eggs", "done": False},
    {"id": 2, "title": "Workout", "description": "Go for a run", "done": True},
    {"id": 3, "title": "Read book", "description": "Finish the novel", "done": False},
]

def find_task(task_id):
    """Helper function to locate a task by ID."""
    return next((task for task in tasks if task["id"] == task_id), None)

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    """Deletes a task by ID if it exists."""
    task = find_task(task_id)
    if not task:
        abort(404)
    
    tasks.remove(task)
    return jsonify({"message": "Task deleted", "tasks": tasks}), 200

@app.route("/", methods=["GET", "POST"])
def index():
    """Handles task list display and adding new tasks."""
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description", "").strip()
        
        if not title:
            abort(400, "Task title is required")
        
        new_task = {
            "id": tasks[-1]["id"] + 1 if tasks else 1,
            "title": title.strip(),
            "description": description,
            "done": False
        }
        tasks.append(new_task)
        return redirect(url_for("index"))
    
    return render_template("index.html", tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)

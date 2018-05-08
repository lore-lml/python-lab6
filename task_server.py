from flask import Flask, jsonify, abort, request, Response

import db_interaction

app = Flask(__name__)

# ------------ REST API--------------


@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    result = db_interaction.get_tasks()
    tasks = []

    for item in result:
        task = prepare_json(item)
        tasks.append(task)

    return jsonify({'tasks': tasks})

@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    result = db_interaction.get_task(int(task_id))
    if result is not None:
        return jsonify(prepare_json(result))
    else:
        return "CIAO NON ESISTE"


@app.route('/api/tasks', methods=['POST'])
def insert_task():
    new_task = request.json

    if (new_task is not None) and ('description' in new_task) and ('priority' in new_task):
        text = new_task['description']
        urgent = new_task['priority']

        # insert in the database
        db_interaction.insert_task(text, urgent)

        return Response(status=201)

    abort(403)


@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = request.json

    if (task is not None) and ('description' in task) and ('priority' in task):
        text = task['description']
        urgent = task['priority']
        db_interaction.update_task(text, urgent, int(task_id))
        return Response(status=200)

    abort(403)


@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):

    db_interaction.delete_task(task_id)
    return Response(status=200)

def prepare_json(item):
    task = dict()
    task['id'] = item[0]
    task['description'] = item[1]
    task['priority'] = item[2]
    return task


if __name__ == '__main__':
    app.run()
from flask import Flask
from flask_restful import Resource, Api, reqparse, abort

app = Flask(__name__)
api = Api(app)

todos = {
    1: {'task': "Write hello world program", 'summary': "writing the coding using by python"},
    2: {'task': "are you like python", 'summary': "yeah i like python "},
    3: {'task': "do you like flutter", 'summary': "yes i like fluttter and python"},

}

task_past_args = reqparse.RequestParser()
task_past_args.add_argument('task', type=str, help='task is require.', required=True)
task_past_args.add_argument('summary', type=str, help='summary is require.', required=True)


class ToDo(Resource):
    def get(self, todo_id):
        return todos[todo_id]

    def post(self, todo_id):
        args = task_past_args.parse_args()
        if todo_id in todos:
            abort(409, "Task Id already token")
        todos[todo_id] = {'task': args["task"], 'summary': args["summary"]}
        return todos[todo_id]


api.add_resource(ToDo, '/todos/<int:todo_id>')


class ToDosList(Resource):

    def get(self):
        return todos


api.add_resource(ToDosList, '/todos')

if __name__ == '__main__':
    app.run(debug=True)

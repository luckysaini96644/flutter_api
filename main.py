from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return "hello lucky"


@app.route("/index")
def lucky():
    name = 'lucky'
    return render_template("index.html",name = name)


if __name__ == '__main__':
    app.run(debug=True)

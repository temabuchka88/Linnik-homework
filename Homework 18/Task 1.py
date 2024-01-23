from flask import Flask

app = Flask(__name__)

a = 0


@app.route("/", methods=["GET"])
def zero():
    return str(a)


@app.route("/plus", methods=["POST"])
def plus_one():
    global a
    a += 1
    return str(a)


@app.route("/minus", methods=["POST"])
def minus_one():
    global a
    a -= 1
    return str(a)


if __name__ == "__main__":
    app.run()

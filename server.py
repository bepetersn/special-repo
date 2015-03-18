

from flask import Flask, request

app = Flask(__name__)

@app.route("/api/request-coffee", methods=['POST'])
def hello():
    print request.form.keys()
    print request.files.keys()


if __name__ == "__main__":
    app.run()
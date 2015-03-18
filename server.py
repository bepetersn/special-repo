

from flask import Flask, request

app = Flask(__name__)

@app.route("/api/request-coffee", methods=['POST'])
def hello():

    # Oddly, `request.form` has a `None` key that has the
    # contents of the file that was posted, while
    # `request.files` is empty.

    print('request.form: {}'.format(request.form.keys()))
    print('request.files: {}'.format(request.files.keys()))
    import pdb; pdb.set_trace()


if __name__ == "__main__":
    app.run()

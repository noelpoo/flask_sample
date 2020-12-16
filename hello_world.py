from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return "hello, world!", 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)

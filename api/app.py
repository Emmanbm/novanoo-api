from flask import Flask, jsonify
# from flask_cors import CORS
from objects.functions import get_users

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({
        'message': 'Hello Novanoo !',
        'code': 200
    }), 200


@app.route('/users')
def users():
    return jsonify({
        "message": "Success",
        "code": 200,
        "data": get_users()
    })


@app.route('/test')
def test():
    return jsonify({
        "message": "Test",
        "code": 200
    })


if __name__ == '__main__':
    app.run(debug=True)

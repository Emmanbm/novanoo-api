from flask import Flask, jsonify
# from flask_cors import CORS

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'message': 'Hello world',
        'code': 200
    }), 200

@app.route('/about')
def about():
    return jsonify({
        "message": "About",
        "code": 200
    })

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)

"""
Enable CORS in order for the flask server to receive requests
from frontend server
"""
CORS(app, origins="https://localhost:5001")

@app.route('/', methods=[POST])
def home_test():
    return jsonify({'message': 'hello from backend'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
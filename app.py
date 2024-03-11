from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def hello():
    greeting = os.getenv('GREETING', 'Hello, World!')
    return greeting

@app.route("/data")
def data():
    sample_data = {
        "samples": [
            {"name": "one", "id": "7692c3ad3540bb803c020b3aee66cd8887123234ea0c6e7143c0add73ff431ed"},
            {"name": "two", "id": "3fc4ccfe745870e2c0d99f71f30ff0656c8dedd41cc1d7d3d376b0dbe685e2f3"},
            {"name": "three", "id": "8b5b9db0c13db24256c829aa364aa90c6d2eba318b9232a4ab9313b954d3555f"}
        ]
    }
    return jsonify(sample_data)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

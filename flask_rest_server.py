from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    data = request.json
    result = data['a'] + data['b']
    return jsonify(result=result)

@app.route('/subtract', methods=['POST'])
def subtract():
    data = request.json
    result = data['a'] - data['b']
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
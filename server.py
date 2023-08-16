from flask import Flask, request

app = Flask(__name__)

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return "Welcome to the Calculator App!"

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.json  # Assuming you're sending JSON data in the request body
    if 'numbers' in data and isinstance(data['numbers'], list):
        result = sum(data['numbers'])
        return {"result": result}
    else:
        return {"error": "Invalid data"}

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.json
    if 'numbers' in data and isinstance(data['numbers'], list) and len(data['numbers']) >= 2:
        result = data['numbers'][0] - sum(data['numbers'][1:])
        return {"result": result}
    else:
        return {"error": "Invalid data"}

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')

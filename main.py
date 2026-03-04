from flask import Flask, request, jsonify

app = Flask(__name__)

def add(a, b):
    return a + b

@app.route('/')
def home():
    return "Calculator App is Running!"

@app.route('/add')
def sum_route():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    result = add(a, b)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

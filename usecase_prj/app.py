from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/hello", methods=["GET"])
def hello_world():
    return jsonify({"message": "Hello World"})


@app.route("/concatenate", methods=["POST"])
def concatenate_strings():
    data = request.get_json()
    str1 = data.get("string1", "")
    str2 = data.get("string2", "")
    result = str1 + str2
    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)
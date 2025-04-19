

from flask import Flask, request, jsonify
from logic import calculate_minimum_cost

app = Flask(__name__)

@app.route("/calculate-cost", methods=["POST"])
def calculate_cost():
    order = request.get_json()
    if not order:
        return jsonify({"error": "Invalid or empty request"}), 400

    try:
        cost = calculate_minimum_cost(order)
        return jsonify({"minimum_cost": cost})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

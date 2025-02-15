from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

disease_data = {
    "American Bollworm on Cotton": {
        "chemicals": ["Cypermethrin", "Chlorantraniliprole"],
        "preventive_measures": [
            "Crop rotation", 
            "Resistant varieties", 
            "Use of pheromone traps (5-10 per hectare)",
            "Deep plowing during summer to expose hibernating larvae"
        ],
        "herbal_remedies": ["Neem oil", "Garlic extract", "Tulsi leaf extract (10%) as repellent"], 
        "yield_risk": ["high"],
        "additional": [
            {"Identification": "Look for circular holes in bolls and presence of green caterpillars"}, 
            {"Economic Threshold": "5-10% damaged bolls or 1 larva per plant"},
            {"Best Treatment Time": "Early morning or late evening"}
        ]
    },
    "Army worm": {
        "chemicals": {
            "Emamectin benzoate": ["Proclaim 5% SG", "Promec 1.9% EC", "Emstar 5% SG"],
            "Spinetoram": ["Delegate 25% WG", "Radiant 12% SC"]
        },
        "preventive_measures": [
            "Monitor fields regularly for egg masses and young larvae",
            "Maintain field sanitation and weed control"
        ],
        "herbal_remedies": [
            "Neem oil spray (2-3% concentration)",
            "Castor leaf extract (10%)"
        ],
        "yield_risk": ["High"],
        "additional": [
            {"Identification": "Irregular holes in leaves"}
        ]
    }
}

# @app.route('/get_disease_info', methods=['POST'])
# def get_disease_info():
#     data = request.json
#     disease_name = data.get('disease_name')
    
#     if not disease_name:
#         return jsonify({"error": "Disease name is required"}), 400

#     disease_info = disease_data.get(disease_name)
#     if disease_info:
#         return jsonify(disease_info)
#     else:
#         return jsonify({"error": "Disease not found"}), 404
@app.route('/get_disease_info', methods=['GET', 'POST'])
def get_disease_info():
    disease_name = request.args.get('disease_name') if request.method == 'GET' else request.json.get('disease_name')
    
    if not disease_name:
        return jsonify({"error": "Disease name is required"}), 400

    disease_info = disease_data.get(disease_name)
    return jsonify(disease_info) if disease_info else jsonify({"error": "Disease not found"}), 404


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

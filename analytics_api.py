# analytics_api.py
from flask import Flask, jsonify
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

app = Flask(__name__)

def get_aggregated_analytics():
    return {
        "total_clubs": 25,
        "total_members": 100000,
        "average_transactions_per_member": 3,
        "total_points_accrued": 500000,
        "referral_conversion_rate": 0.2
    }

try:
    model = load_model('poontoz_model.h5')
except Exception as e:
    print("Model could not be loaded:", e)
    model = None

def get_ml_predictions():
    sample_features = np.array([[200, 5, 2]])
    if model:
        prediction = model.predict(sample_features)
        return float(prediction[0][0])
    else:
        return None

@app.route('/api/analytics', methods=['GET'])
def analytics():
    data = get_aggregated_analytics()
    return jsonify(data)

@app.route('/api/predictions', methods=['GET'])
def predictions():
    pred = get_ml_predictions()
    if pred is not None:
        return jsonify({"predicted_engagement_score": pred})
    else:
        return jsonify({"error": "ML model not available"}), 500

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "API is running"})

if __name__ == '__main__':
    app.run(debug=True, port=8060)

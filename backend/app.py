from flask import Flask, jsonify
from flask_cors import CORS
from quantum import QuantumRNG
import os

app = Flask(__name__)
CORS(app)

quantum_rng = QuantumRNG()

@app.route('/generate/<int:num_bits>', methods=['GET'])
def generate_number(num_bits):
    if num_bits < 1 or num_bits > 8:
        return jsonify({'error': 'Number of bits must be between 1 and 8'}), 400

    result = quantum_rng.generate_random_number(num_bits)
    return jsonify(result)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

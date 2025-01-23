from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute
from qiskit.providers.qbraid import QbraidProvider
import os

class QuantumRNG:
    def __init__(self):
        self.provider = QbraidProvider()

    def create_quantum_circuit(self, num_bits):
        """Create a quantum circuit for generating random numbers"""
        q = QuantumRegister(num_bits)
        c = ClassicalRegister(num_bits)
        circuit = QuantumCircuit(q, c)

        # Apply Hadamard gates to create superposition
        for i in range(num_bits):
            circuit.h(q[i])

        # Measure qubits
        circuit.measure(q, c) 
        
        return circuit

    def generate_random_number(self, num_bits=4, shots=1):
        """Generate a random number using quantum circuit"""
        try:
            # Create and execute the circuit
            circuit = self.create_quantum_circuit(num_bits)
            job = execute(circuit,
                          backend=self.provider.get_backend('simulator'),
                          shots=shots)
            result = job.result()

            # Get the counts of measurement
            counts = result.get_counts(circuit)

            # Convert binary string to decimal
            # Take the first result if multiple shots
            binary_result = list(counts.keys())[0]
            decimal_result = int(binary_result, 2)

            return {
                'decimal': decimal_result,
                'binary': binary_result,
                'max_value': 2**num_bits - 1
            }

    except Exception as e:
            return {'error': str(e)}

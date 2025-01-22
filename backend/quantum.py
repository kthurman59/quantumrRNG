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


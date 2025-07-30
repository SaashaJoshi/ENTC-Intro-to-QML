"""Utility functions for VQC"""

from qiskit.circuit import QuantumCircuit


# Data Embedding - Angle Encoding
def angle_embedding(feature_dims: int, feature_param: list):
    embedding = QuantumCircuit(feature_dims)

    for qubit in range(feature_dims):
        embedding.ry(feature_param[qubit], qubit)
    return embedding
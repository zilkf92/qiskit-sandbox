import matplotlib.pyplot as plt
import numpy as np

from qiskit import IBMQ, Aer, assemble, transpile
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.providers.ibmq import least_busy

from qiskit.visualization import plot_histogram

n = 2
grover_circuit = QuantumCircuit(n)


def initialize(qc, qubits):
    """Apply a H-gate to 'qubits' in qc"""
    for q in qubits:
        qc.h(q)
    return qc


grover_circuit = initialize(grover_circuit, [0, 1])

grover_circuit.cz(0, 1)
grover_circuit.rz(-np.pi, 0)
grover_circuit.rz(-np.pi, 1)
grover_circuit.h([0, 1])
grover_circuit.cz(0, 1)
grover_circuit.z([0, 1])
grover_circuit.h([0, 1])
print(grover_circuit)

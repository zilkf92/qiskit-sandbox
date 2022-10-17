import matplotlib.pyplot as plt
import numpy as np

from qiskit import IBMQ, Aer, assemble, transpile
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.providers.ibmq import least_busy

from qiskit.visualization import plot_histogram

n = 2
grover_circuit = QuantumCircuit(n)

grover_circuit.h([0, 1])
grover_circuit.cz(0, 1)
grover_circuit.rz(-np.pi, 0)
grover_circuit.rz(-np.pi, 1)
grover_circuit.h([0, 1])
grover_circuit.x([0, 1])
grover_circuit.h(1)
grover_circuit.cx(0, 1)
grover_circuit.h(1)
grover_circuit.x([0, 1])
grover_circuit.h([0, 1])
print(grover_circuit)

basis_gates = ["rz", "rx", "h", "cz", "cx"]

qc_trans = transpile(grover_circuit, basis_gates=basis_gates)
print(qc_trans)

qasm_express = qc_trans.qasm()
print(qasm_express)

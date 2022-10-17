import numpy as np

from qiskit import QuantumCircuit
from qiskit.compiler import transpile
from qiskit.providers.aer import QasmSimulator
from qiskit.circuit.library.basis_change import qft


simulator = QasmSimulator()

circ = qft.QFT(9)
print(circ)

basis_gates = ["rz", "rx", "h", "cz", "cx"]

qc_trans = transpile(circ, basis_gates=basis_gates)
print(qc_trans)

qasm_express = qc_trans.qasm()
print(qasm_express)

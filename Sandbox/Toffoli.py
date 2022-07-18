import numpy as np

from qiskit import QuantumCircuit
from qiskit.compiler import transpile
from qiskit.providers.aer import QasmSimulator


simulator = QasmSimulator()

circ = QuantumCircuit(3)
circ.ccx(0, 1, 2)
print(circ)

basis_gates = ["rz", "rx", "h", "cz"]

qc_trans = transpile(circ, basis_gates=basis_gates)
print(qc_trans)

qasm_express = qc_trans.qasm()
print(qasm_express)

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit.compiler import transpile
from numpy import pi

qreg_q = QuantumRegister(2, 'q')
creg_c = ClassicalRegister(2, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.h(qreg_q[0])
circuit.x(qreg_q[1])
circuit.h(qreg_q[1])
circuit.cx(qreg_q[0], qreg_q[1])

print(circuit)

basis_gates = ["rz", "rx", "h", "cz", "cx"]

qc_trans = transpile(circuit, basis_gates=basis_gates)
print(qc_trans)

qasm_express = qc_trans.qasm()
print(qasm_express)
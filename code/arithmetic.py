# Half Adder Logic (Classical)
def half_adder(a, b):
    sum_ = a ^ b  # XOR gate
    carry = a & b  # AND gate
    return sum_, carry

# Full Adder Logic (Classical)
def full_adder(a, b, cin):
    sum_ = a ^ b ^ cin  # XOR gates
    carry = (a & b) | (cin & (a ^ b))  # AND and OR gates
    return sum_, carry

from qiskit import QuantumCircuit

def quantum_half_adder():
    # Create a quantum circuit with 2 qubits (inputs) and 2 classical bits (output)
    qc = QuantumCircuit(2, 2)

    # Apply the CNOT gate to implement XOR (Sum)
    qc.cx(0, 1)  # A XOR B for Sum

    # Apply Toffoli gate to implement AND (Carry)
    qc.ccx(0, 1, 1)  # A AND B for Carry

    # Measure the qubits
    qc.measure(0, 0)  # Sum output
    qc.measure(1, 1)  # Carry output

    return qc

def quantum_full_adder():
    # Create a quantum circuit with 3 qubits (inputs) and 2 classical bits (outputs)
    qc = QuantumCircuit(3, 2)

    # Apply the first CNOT gate (A XOR B) for sum
    qc.cx(0, 1)  # A XOR B

    # Apply the second CNOT gate (A XOR B XOR Cin) for sum
    qc.cx(1, 2)  # (A XOR B) XOR Cin

    # Apply Toffoli gate for carry
    qc.ccx(0, 1, 2)  # A AND B for Carry

    # Measure the qubits
    qc.measure(0, 0)  # Sum output
    qc.measure(1, 1)  # Carry output

    return qc


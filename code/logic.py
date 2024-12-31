from qiskit import QuantumCircuit, transpile
from qiskit.providers.aer import AerSimulator


def logical_and():
    """
    Creates a quantum circuit to perform a logical AND operation using a Toffoli gate.
    """
    qc = QuantumCircuit(3, 1)  # 3 qubits: 2 inputs, 1 output; 1 classical bit for measurement

    # Set the input qubits to desired values (for example, True and True)
    qc.x(0)  # Set the first input to 1 (True)
    qc.x(1)  # Set the second input to 1 (True)

    # Perform AND operation: If both input qubits are 1, set the third qubit to 1
    qc.ccx(0, 1, 2)

    # Measure the output
    qc.measure(2, 0)
    return qc

def logical_or():
    """
    Creates a quantum circuit to perform a logical OR operation.
    """
    qc = QuantumCircuit(3, 1)  # 3 qubits: 2 inputs, 1 output; 1 classical bit for measurement

    # Set the input qubits to desired values (for example, True and False)
    qc.x(0)  # Set the first input to 1 (True)

    # Perform OR operation: Use a combination of gates to simulate OR logic
    # Output is true if at least one input is true
    qc.cx(0, 2)
    qc.cx(1, 2)

    # Measure the output
    qc.measure(2, 0)
    return qc

def logical_not():
    """
    Creates a quantum circuit to perform a logical NOT operation.
    """
    qc = QuantumCircuit(1, 1)  # 1 qubit: input; 1 classical bit for measurement

    # Set the input qubit to desired value (for example, True)
    qc.x(0)  # Set the input to 1 (True)

    # Perform NOT operation: Flip the input qubit
    qc.x(0)

    # Measure the output
    qc.measure(0, 0)
    return qc

# Function to simulate a circuit
def run_circuit(qc):
    simulator = AerSimulator()
    # Transpile the circuit for the AerSimulator
    compiled_circuit = transpile(qc, simulator)
    # Run the simulation
    result = simulator.run(compiled_circuit, shots=1).result()
    counts = result.get_counts()
    return counts

# Logical AND Example
qc_and = logical_and()
print("Logical AND Circuit:")
print(qc_and)
print("Results:", run_circuit(qc_and))

# Logical OR Example
qc_or = logical_or()
print("\nLogical OR Circuit:")
print(qc_or)
print("Results:", run_circuit(qc_or))

# Logical NOT Example
qc_not = logical_not()
print("\nLogical NOT Circuit:")
print(qc_not)
print("Results:", run_circuit(qc_not))

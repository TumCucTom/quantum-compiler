import os
from qiskit import QuantumCircuit, Aer, execute

def quantum_multiplication():
    # Create a quantum circuit with 4 qubits for the result and 4 classical bits for measurement
    qc = QuantumCircuit(4, 4)

    # Inputs (A = a1a0, B = b1b0) will be applied to qubits
    # A = a1a0, B = b1b0 -> We'll assume inputs are in |00>, |01>, |10>, or |11>

    # Step 1: Multiply a0 * b0 -> c0
    qc.cx(0, 3)  # a0 AND b0

    # Step 2: Multiply a0 * b1 -> intermediate and add
    qc.cx(1, 2)  # a0 AND b1 -> Intermediate result

    # Step 3: Multiply a1 * b0 -> intermediate and add
    qc.cx(2, 3)  # a1 AND b0 -> Intermediate result

    # Step 4: Multiply a1 * b1 -> c3 (final result)
    qc.cx(1, 3)  # a1 AND b1 -> Final result

    # Measure the qubits to get the result
    qc.measure([0, 1, 2, 3], [0, 1, 2, 3])  # Measure the result qubits

    return qc

def quantum_multiplication_calc(a1_val, a0_val, b1_val, b0_val):
    """
    Creates a quantum circuit that performs 2-bit multiplication.

    The inputs are:
        a1, a0: Representing the 2 bits of number A
        b1, b0: Representing the 2 bits of number B
    The output is:
        p3, p2, p1, p0: Representing the 4 bits of the product P

    Returns:
        QuantumCircuit: A Qiskit QuantumCircuit object implementing the multiplier
    """
    # Number of qubits:
    # 4 for the inputs (a1, a0, b1, b0) + 4 for the product (p3, p2, p1, p0)
    # Using ancillary qubits for intermediate calculations
    circuit = QuantumCircuit(8, 4)

    # Define the qubits for clarity
    a1, a0, b1, b0 = 0, 1, 2, 3  # Input qubits
    p0, p1, p2, p3 = 4, 5, 6, 7  # Product qubits

    # Initialize the qubits with the input values (a1_val, a0_val, b1_val, b0_val)
    if a1_val == 1:
        circuit.x(a1)
    if a0_val == 1:
        circuit.x(a0)
    if b1_val == 1:
        circuit.x(b1)
    if b0_val == 1:
        circuit.x(b0)

    # Step 1: Compute p0 = a0 AND b0
    circuit.ccx(a0, b0, p0)

    # Step 2: Compute intermediate values for p1
    circuit.ccx(a1, b0, p1)  # Contribution of a1*b0 to p1
    circuit.ccx(a0, b1, p1)  # Contribution of a0*b1 to p1

    # Step 3: Compute intermediate values for p2
    circuit.ccx(a1, b1, p2)  # Contribution of a1*b1 to p2
    # Combine contributions from carry-over for p2 (using ancillary qubits if needed)

    # Step 4: Compute the highest bit p3 (carry from p2)
    # Add logic gates for final carry propagation if required

    # (Optional) Measure product qubits if needed
    circuit.measure([p0, p1, p2, p3], [0, 1, 2, 3])

    print(circuit)

    # Execute the circuit on a quantum simulator
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(circuit, simulator, shots=1).result()

    # Return the measured output
    return result.get_counts()

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

# Quantum Multiplication Test
def run_quantum_multiplication(qc):
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(qc, simulator, shots=1).result()
    counts = result.get_counts()
    return counts

# Function to test the quantum full adder
def test_quantum_full_adder():
    # Set all possible input combinations (A, B, Cin)
    input_combinations = [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1),
                          (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]

    simulator = Aer.get_backend('qasm_simulator')

    # Prepare the output directory
    output_dir = "../output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(os.path.join(output_dir, "circuits-out.txt"), "w") as f:
        # For each combination, create the quantum full adder circuit and execute it
        for A, B, Cin in input_combinations:
            # Create the quantum full adder circuit
            qc = quantum_full_adder()

            # Set the initial states of the qubits based on the input combination
            # A, B, Cin are the input qubits
            if A == 1:
                qc.x(0)  # Set qubit A to 1
            if B == 1:
                qc.x(1)  # Set qubit B to 1
            if Cin == 1:
                qc.x(2)  # Set qubit Cin to 1

            # Draw the quantum circuit and save it to file
            circuit_draw = qc.draw(output='text')  # Text-based representation of the circuit
            f.write(f"Input (A={A}, B={B}, Cin={Cin}) => Quantum Circuit:\n")
            f.write(str(circuit_draw) + "\n\n")  # Convert TextDrawing to string

            # Execute the circuit
            result = execute(qc, simulator, shots=1).result()
            counts = result.get_counts()

            # Write the result to the file
            f.write(f"Results: {counts}\n\n")

def quantum_mult_calc_run(a1, a0, b1, b0):
    output = quantum_multiplication_calc(a1, a0, b1, b0)
    print(f"Quantum multiplication result for A={a1}{a0}, B={b1}{b0}: {output}")

# Run the test and save the circuit to the file
test_quantum_full_adder()

# Test Quantum Multiplication
qc_multiplication = quantum_multiplication()
print("Quantum Multiplication Circuit:")
print(qc_multiplication)
print("Results:", run_quantum_multiplication(qc_multiplication))

# Test the quantum multiplication function
a1, a0 = 1, 0  # Binary 3
b1, b0 = 1, 0  # Binary 2
quantum_mult_calc_run(a1,a0,b1,b0)

from qiskit import Aer, execute

def test_quantum_multiplication():
    # Define all possible 2-bit inputs for a and b (values 0 to 3)
    for a1_val in range(2):  # a1_val is either 0 or 1
        for a0_val in range(2):  # a0_val is either 0 or 1
            for b1_val in range(2):  # b1_val is either 0 or 1
                for b0_val in range(2):  # b0_val is either 0 or 1
                    # Calculate expected product
                    a = a1_val * 2 + a0_val  # Convert the 2-bit input a to a number
                    b = b1_val * 2 + b0_val  # Convert the 2-bit input b to a number
                    expected_product = a * b  # Multiply the two numbers

                    # Get quantum multiplication result
                    result = quantum_multiplication_calc(a1_val, a0_val, b1_val, b0_val)

                    # Extract the result as a 4-bit string (p3 p2 p1 p0)
                    measured_bits = list(result.keys())[0]
                    measured_product = int(measured_bits, 2)

                    # Compare the expected and measured results
                    assert measured_product == expected_product, \
                        f"Test failed for inputs A: ({a1_val},{a0_val}) and B: ({b1_val},{b0_val}). " \
                        f"Expected: {expected_product}, Got: {measured_product}"

                    print(f"Test passed for inputs A: ({a1_val},{a0_val}) and B: ({b1_val},{b0_val}). " \
                          f"Product: {expected_product}")

# Call the test function
test_quantum_multiplication()

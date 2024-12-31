# Quantum Compiler

## Overview
This project aims to build a basic quantum compiler that translates classical algorithms into quantum circuits. Quantum compilers are highly advanced and in demand, especially with the growing interest in hybrid quantum-classical algorithms. By working on this project, you will demonstrate the ability to design low-level systems for quantum hardware.

---

## Features
- **Classical Algorithm Parsing:** Parse classical algorithms into an intermediate representation (IR).
- **Quantum Translation:** Map classical operations to quantum gates.
- **Circuit Optimization:** Minimize gate count and circuit depth for efficient execution on quantum hardware.
- **Quantum Circuit Output:** Generate and visualize quantum circuits using Qiskit.

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/quantum-compiler.git
   cd quantum-compiler
   ```

2. Set up the environment:
   ```bash
   pip install qiskit qiskit-aer
   ```

---

## Usage

### Input: Classical Algorithm Specification
- Algorithms can be written in a high-level pseudocode or Python functions.
- Example input:
  ```python
  algorithm = {
      "operations": [
          {"type": "AND", "qubits": [0, 1, 2]},
          {"type": "NOT", "qubits": [0]}
      ],
      "qubits": 3
  }
  ```

### Translating to Quantum Circuits
Use the provided function to convert the algorithm:
```python
from compiler import classical_to_quantum

qc = classical_to_quantum(algorithm)
qc.draw()  # Visualize the circuit
```

### Simulating Quantum Circuits
Run the generated circuit on a simulator:
```python
from qiskit import Aer, execute

simulator = Aer.get_backend("qasm_simulator")
result = execute(qc, simulator).result()
print(result.get_counts())
```

---

## How It Works

### Pipeline
1. **Input Parsing:**
    - Parses classical algorithms into an intermediate representation (IR).
    - Example: Convert operations like "compare" or "increment" into structured steps.

2. **Quantum Translation:**
    - Maps classical operations to quantum gates using predefined rules:
        - Logical operations (AND/OR/NOT) → Toffoli or CNOT gates.
        - Arithmetic operations → Quantum adders or multipliers.
    - Ensures all operations are reversible.

3. **Circuit Optimization:**
    - Reduces gate count and depth using quantum optimization techniques (e.g., gate fusion).

4. **Output Generation:**
    - Outputs a quantum circuit compatible with Qiskit.
    - Provides a visualization of the circuit.

---

## Examples
### Translating an AND Operation
Input:
```python
algorithm = {
    "operations": [
        {"type": "AND", "qubits": [0, 1, 2]}
    ],
    "qubits": 3
}
```

Generated Circuit:
```text
     q_0: ───■───
              │
     q_1: ───■───
              │
     q_2: ───X───
```

---

## Challenges
- **Reversibility:** Classical operations are not inherently reversible. Ancilla qubits are used to store intermediate states.
- **Scalability:** Large algorithms require many qubits. Start with small, modular implementations.
- **Optimization:** Minimize gate count and depth for practical execution on real quantum hardware.

---

## Future Extensions
- Add support for complex algorithms like Grover's Search or Shor's Algorithm.
- Implement hybrid quantum-classical functionality for pre-processing and optimization.
- Explore integration with additional quantum libraries like Cirq or Braket.

---

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests to enhance the functionality or [email me](hf23482@bristol.ac.uk) at hf23482@bristol.ac.uk.

---

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## Acknowledgments
This project leverages Qiskit for quantum circuit generation and simulation. Special thanks to the open-source quantum computing community for resources and inspiration.

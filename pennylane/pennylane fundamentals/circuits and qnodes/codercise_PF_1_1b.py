import pennylane as qml

dev_qubit = qml.device("default.qubit", wires = ["alice", "bob"])
dev_mixed = qml.device("default.mixed", wires = 2)

@qml.qnode(dev_qubit)
def example_circuit(theta):
    qml.RX(theta, wires = "alice")
    qml.CNOT(wires = ["alice", "bob"])
    return qml.state()

print(example_circuit(0.3))
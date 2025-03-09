import pennylane as qml
from codercise_PF_1_1a import circuit

dev = qml.device("default.qubit", wires = 2)

# calling function from different module
circuit_qnode = qml.QNode(circuit, dev)

# since print statement in other module, runs it too upon call
print(circuit_qnode(0.3))
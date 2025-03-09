import pennylane as qml

def subcircuit_1(angle):
    qml.RX(angle, wires = 0)
    qml.Y(wires = 1)

def subcircuit_2():
    qml.Hadamard(wires = 0)
    qml.CNOT(wires = [0, 1])

dev = qml.device("default.qubit", wires = 2)

@qml.qnode(dev)
def full_circuit(theta, phi):
    subcircuit_1(theta)
    subcircuit_2()
    subcircuit_1(phi)

    return qml.state()
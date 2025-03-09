import pennylane as qml

def subcircuit_1(angle, wire_list):
    qml.RX(angle, wires = wire_list[0])
    qml.Y(wires = wire_list[1])

def subcircuit_2(wire_list):
    qml.Hadamard(wires = wire_list[0])
    qml.CNOT(wires = wire_list)

# using wirelist, to allow flipping components between wires when calling subcircuits
dev = qml.device("default.qubit", wires = [0, 1])

@qml.qnode(dev)
def full_circuit(theta, phi):
    subcircuit_1(theta, [0, 1])
    subcircuit_2([0, 1])
    # flipping wires, compared to first subcircuit call
    subcircuit_1(phi, [1, 0])

    return qml.state()
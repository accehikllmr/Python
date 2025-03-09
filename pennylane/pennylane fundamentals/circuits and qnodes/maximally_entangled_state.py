import pennylane as qml

# creating Device object, but given wires specific names instead of numbers
dev_c_t = qml.device("default.qubit", wires = ["target", "control"])

@qml.qnode(dev_c_t)
# function for maximally entangled state
def create_entangled():
    qml.Hadamard(wires = "control")
    qml.CNOT(wires = ["control", "target"])
    return qml.state()

print(create_entangled())
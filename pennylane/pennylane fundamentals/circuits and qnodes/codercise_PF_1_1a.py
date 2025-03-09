import pennylane as qml
from pennylane import numpy as np

dev = qml.device("default.qubit", wires = 2)

@qml.qnode(dev)
def circuit(phi):
    '''
    This quantum function implements a circuit and returns the output quantum state.
    '''
    qml.Hadamard(wires = 0)
    qml.X(wires = 1)
    qml.CNOT(wires = [0, 1])
    qml.RY(phi, wires = 1)

    return qml.state()

print(qml.draw(circuit)(np.pi/2))
import pennylane as qml
from pennylane import numpy as np

# instantiating Device object, passing number fo wires to constructor
dev = qml.device("default.qubit", wires = 2)

# decorator below pairs quantum circuit with quantum device (called a qNode)
@qml.qnode(dev)
# quantum function, otherwise known as a quantum circuit
def my_first_quantum_function(theta):
    '''
    gates attached to same number wire are connected by said wire
    wires are assigned from top to bottom, as organized below
    '''
    # instantiating Gate objects, passing wire number to constructor
    qml.RX(theta, wires = 0)
    qml.Hadamard(wires = 0)
    qml.PauliY(wires = 1)
    qml.Hadamard(wires = 1)

    # returns a complex array (using numpy) which represents quantum states
    return qml.state()

print(my_first_quantum_function(np.pi/4))

my_first_qnode = qml.QNode(my_first_quantum_function, dev)
print(my_first_qnode(np.pi/4))
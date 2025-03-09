import pennylane as qml

def subcircuit_1(angle):
    qml.RX(angle, wires = 0)
    qml.PauliY(wires = 1)

def subcircuit_2():
    qml.Hadamard(wires = 0)
    qml.CNOT(wires = [0, 1])

'''
for circuits which have repeating parts, it is more efficient to create
subcircuits which can be called repeatedly when constructing the full circuit
'''
def full_circuit(theta, phi):
    subcircuit_1(theta)
    subcircuit_2()
    subcircuit_1(phi)

# drawing the circuit, passing arguments (in radians) to function parameters
print(qml.draw(full_circuit)(0.3, 0.2))
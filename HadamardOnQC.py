from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute
from qiskit_ibm_provider import IBMProvider
from matplotlib import pyplot as plt
from numpy import pi

with(open('token') as f):
        token = f.readline()
        f.close()

print("Connecting...")
IBMProvider.save_account(token=token, overwrite=True)
provider = IBMProvider()
backend = provider.get_backend("ibm_nairobi")
print("Connected")

qreg_q = QuantumRegister(2, 'q')
creg_c = ClassicalRegister(2, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.h(qreg_q[0])
circuit.cx(qreg_q[0], qreg_q[1])

circuit.measure(qreg_q[1], creg_c[1])
circuit.measure(qreg_q[0], creg_c[0])

print("Created, launching...")
circuitResult = execute(circuit, backend=backend, shots=1024).result().get_counts(circuit)
print("Done")

print(circuitResult.items())
(results, counts) = zip(*circuitResult.items())
plt.bar(results, counts)
plt.show()
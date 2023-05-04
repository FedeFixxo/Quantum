from qiskit import Aer # Local quantum computer simulator
from qiskit_aer.noise import NoiseModel
from qiskit_ibm_provider import IBMProvider

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute # Registers to handle data
from matplotlib import pyplot as plt
from numpy import pi

def getSimulationDetails(backendName):
    print(f"Retrieving simulation details from {backendName} ...")

    with(open('token') as f):
        token = f.readline()
        f.close()

    IBMProvider.save_account(token=token, overwrite=True)
    provider = IBMProvider()
    backend = provider.get_backend(backendName)
    
    noise = NoiseModel.from_backend(backend)
    topology = backend.configuration().coupling_map

    print(f"Noise and topology imported from {backendName}")
    
    return (noise, topology)


(noise, topology) = getSimulationDetails("ibm_nairobi")
backend = Aer.get_backend("qasm_simulator")

qreg_q = QuantumRegister(2, 'q')
creg_c = ClassicalRegister(2, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.h(qreg_q[0])
circuit.measure(qreg_q[1], creg_c[1])
circuit.measure(qreg_q[0], creg_c[0])

print("Created, simulating...")
circuitResult = execute(circuit, backend=backend, shots=1024, noise_model=noise, coupling_map=topology, basis_gates=noise.basis_gates).result().get_counts(circuit)
print("Done\n")

print(circuitResult.items())
(results, counts) = zip(*circuitResult.items())
plt.bar(results, counts)
plt.show()



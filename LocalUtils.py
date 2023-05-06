from Utils import *
from qiskit import Aer
from qiskit_aer.noise import NoiseModel

class LocalUtils:

    def getSimulationDetails(backendName):
        print(f"Retrieving simulation details from {backendName} ...")
        Utils.connect()
        backend = Utils.getBackend(backendName)
        noise = NoiseModel.from_backend(backend)
        topology = backend.configuration().coupling_map
        
        return (noise, topology)

    def simulate(circuit, backendName="ibm_nairobi", shots=1024, simulationBackendName="qasm_simulator"):
        (noise, topology) = LocalUtils.getSimulationDetails(backendName)
        print("Simulating...", end=" ")
        result = execute(circuit, backend=Aer.get_backend(simulationBackendName) , shots=shots, noise_model=noise, coupling_map=topology, basis_gates=noise.basis_gates).result().get_counts(circuit)
        print("done")
        return result

    def runLocal(circuit, shots=1024, simulationBackendName="qasm_simulator"):
        print("Simulating...", end=" ")
        result = execute(circuit, backend=Aer.get_backend(simulationBackendName) , shots=shots).result().get_counts(circuit)
        print("done")
        return result
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute
from qiskit_ibm_provider import IBMProvider
from matplotlib import pyplot as plt
from numpy import pi

class Utils:
    __token = None
    __backend = None

    def __getToken(fileName="token"):
        try:
            with open(fileName) as f:
                Utils.__token = f.readline()
        except :
            pass

    def __connect(backendName):
        if Utils.__token == None:
            Utils.__getToken()
            if Utils.__token == None:
                print("No token found")
                return
        IBMProvider.save_account(token=Utils.__token, overwrite=True)
        print("Connecting", end=" ")
        provider = IBMProvider()
        print(f"& getting: {backendName}...", end="\t")
        Utils.__backend = provider.get_backend(backendName)
        print("Ready")

    def run(circuit, backendName="ibm_nairobi", shots=1024):
        Utils.__connect(backendName)
        print("Executing...", end=" ")
        result = execute(circuit, backend=Utils.__backend, shots=shots).result().get_counts(circuit)
        print("done")
        return result

    def plotCountBars(circuitResult):
        (results, counts) = zip(*circuitResult.items())
        plt.bar(results, counts)
        plt.show()
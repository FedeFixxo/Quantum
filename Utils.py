from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute
from qiskit_ibm_provider import IBMProvider
from matplotlib import pyplot as plt
from numpy import pi

class Utils:
    __token = None
    __backend = None

    def getToken(fileName="token"):
        try:
            if Utils.__token != None:
                return Utils.__token
            with open(fileName) as f:
                Utils.__token = f.readline()
                return Utils.__token
        except :
            pass

    def connect():
        Utils.getToken()
        IBMProvider.save_account(token=Utils.__token, overwrite=True)

    def getBackend(backendName):
        print("Connecting", end=" ")
        provider = IBMProvider()
        print(f"& getting: {backendName}...", end="\t")
        Utils.__backend = provider.get_backend(backendName)
        print("done")
        return Utils.__backend

    def run(circuit, backendName="ibm_nairobi", shots=1024):
        Utils.connect()
        Utils.getBackend(backendName)
        print("Executing...", end=" ")
        result = execute(circuit, backend=Utils.__backend, shots=shots).result().get_counts(circuit)
        print("done")
        return result

    def plotCountBars(circuitResult):
        (results, counts) = zip(*circuitResult.items())
        plt.bar(results, counts)
        plt.show()
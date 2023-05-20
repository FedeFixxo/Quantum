from LocalUtils import *
from sys import argv, exit

def main():
    configuration = assertInputFormat(argv[1]) if len(argv) > 1 else "0000"

    qreg_q = QuantumRegister(len(configuration) + 1, 'q')
    creg_c = ClassicalRegister(len(configuration), 'c')
    circuit = QuantumCircuit(qreg_q, creg_c)

    setupDJ(circuit, qreg_q)
    controlledFunction(configuration, circuit, qreg_q)
    unmeasuredCircuit = circuit.draw(output="text")
    measure(circuit, qreg_q, creg_c)

    res = LocalUtils.simulate(circuit)
    print(unmeasuredCircuit)
    print(res)
    Utils.plotCountBars(res)


def assertInputFormat(userInput):
    for char in userInput:
        if char != '0' and char != '1':
            exit("Error in user input")
    return userInput

def measure(circuit, qReg, cReg):
    # End of algorithm
    for qbitIndex in range(qReg.size - 1): # Hadamard on all x qbits
        circuit.h(qReg[qbitIndex])
        circuit.measure(qReg[qbitIndex], cReg[qbitIndex])


def controlledFunction(format, circuit, qReg):
    # Set up function
    for qbitIndex in range(qReg.size-1):
        if format[qbitIndex] != "0" :
            circuit.x(qReg[qbitIndex])
        circuit.cx(qReg[qbitIndex], qReg[-1])
        if format[qbitIndex] != "0" :
            circuit.x(qReg[qbitIndex])


def setupDJ(circuit, qReg):
    # Setup |+> on x and |-> on y

    circuit.x(qReg[-1]) # |1> on y
    for qbitIndex in range(qReg.size): # Hadamard on all qbits
        circuit.h(qReg[qbitIndex])


if __name__ == "__main__" :
    main()
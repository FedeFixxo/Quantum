from LocalUtils import *
from sys import argv, exit

def main():
    configuration = assertInputFormat(argv[1]) if len(argv) > 1 else "0000"

    qreg_q = QuantumRegister(len(configuration) + 1, 'q')
    creg_c = ClassicalRegister(len(configuration), 'c')
    circuit = QuantumCircuit(qreg_q, creg_c)

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
    for qbitIndex in range(qReg.size - 1):
        circuit.measure(qReg[qbitIndex], cReg[qbitIndex])


# Set up oracle's function
def controlledFunction(format, circuit, qReg):
    for qbitIndex in range(qReg.size-1):
        if format[qbitIndex] != "0" :
            circuit.x(qReg[qbitIndex])

        circuit.cx(qReg[-1], qReg[qbitIndex])
        if format[qbitIndex] != "0" :
            circuit.x(qReg[qbitIndex])


if __name__ == "__main__" :
    main()
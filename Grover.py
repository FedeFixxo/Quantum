from LocalUtils import *

def main():
    qreg_q = QuantumRegister(3, 'q')
    creg_c = ClassicalRegister(3, 'c')
    circuit = QuantumCircuit(qreg_q, creg_c)

    hAll(circuit, qreg)
    oracle(circuit, qreg)

    circuit.h(qreg_q[2])
    circuit.ccx(qreg_q[0], qreg_q[1], qreg_q[2])
    circuit.h(qreg_q[2])

    oracle(circuit, qreg)

    hAll(circuit, qreg)
    xAll(circuit, qreg)

    circuit.h(qreg_q[2])
    circuit.ccx(qreg_q[0], qreg_q[1], qreg_q[2])
    circuit.h(qreg_q[2])

    xAll(circuit, qreg)
    hAll(circuit, qreg)
    measure(circuit, qreg, creg)

    res = LocalUtils.simulate(circuit)
    print(res)
    Utils.plotCountBars(res)

def measure(circuit, qreg, creg):
    for i in range(len(qreg)):
        circuit.measure(qreg_q[i], creg_c[i])

def xAll(circuit, qreg):
    for i in range(len(qreg)):
        circuit.x(qreg[i])

def hAll(circuit, qreg):
    for i in range(len(qreg)):
        circuit.h(qreg[i])

def oracle(circuit, qreg):
    circuit.x(qreg[0])

if __name__ == "__main__":
    main()
from LocalUtils import *

def main():
    qreg_q = QuantumRegister(5, 'q')
    creg_c = ClassicalRegister(4, 'c')
    circuit = QuantumCircuit(qreg_q, creg_c)

    setup(circuit, qreg_q)
    oracle(circuit, qreg_q)
    measure(circuit, qreg_q, creg_c)

    res = LocalUtils.simulate(circuit)
    print(res)
    Utils.plotCountBars(res)

def oracle(circuit, qreg_q):
    circuit.cx(qreg_q[1], qreg_q[4])
    circuit.cx(qreg_q[3], qreg_q[4])

# Setting on all qbits in |+> except for the ancillar in |->
def setup(circuit, qreg_q):
    circuit.x(qreg_q[-1])
    for registerIndex in range(qreg_q.size):
        circuit.h(qreg_q[registerIndex])

# Hadamard and z projection on all but the ancillar
def measure(circuit, qreg_q, creg_c):
    for registerIndex in range(qreg_q.size - 1):
        circuit.h(qreg_q[registerIndex])
        circuit.measure(qreg_q[registerIndex], creg_c[registerIndex])

if __name__ == "__main__":
    main()
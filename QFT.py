from LocalUtils import *

qreg_q = QuantumRegister(3, 'q')
creg_c = ClassicalRegister(3, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.x(qreg_q[1])
circuit.x(qreg_q[2])
circuit.h(qreg_q[2])
circuit.cp(pi / 2, qreg_q[2], qreg_q[1])
circuit.cp(pi / 4, qreg_q[2], qreg_q[0])
circuit.h(qreg_q[1])
circuit.cp(pi / 2, qreg_q[1], qreg_q[0])
circuit.h(qreg_q[0])
circuit.measure(qreg_q[0], creg_c[0])
circuit.measure(qreg_q[1], creg_c[1])
circuit.measure(qreg_q[2], creg_c[2])

res = LocalUtils.simulate(circuit)
print(res)
Utils.plotCountBars(res)
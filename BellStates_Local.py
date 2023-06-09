from LocalUtils import *

qreg_q = QuantumRegister(2, 'q')
creg_c = ClassicalRegister(2, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.h(qreg_q[0])
circuit.cx(qreg_q[0], qreg_q[1])

circuit.measure(qreg_q[1], creg_c[1])
circuit.measure(qreg_q[0], creg_c[0])

#Utils.plotCountBars(LocalUtils.simulate(circuit)) # Simulation with noise
Utils.plotCountBars(LocalUtils.runLocal(circuit)) #Simulation without noise
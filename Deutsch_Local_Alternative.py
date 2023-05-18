from LocalUtils import *

qreg_q0 = QuantumRegister(2, 'q')
creg_c0 = ClassicalRegister(2, 'c')
circuit = QuantumCircuit(qreg_q0, creg_c0)

circuit.x(qreg_q0[1])
circuit.cx(qreg_q0[1], qreg_q0[0])
circuit.measure(qreg_q0[0], creg_c0[0])

Utils.plotCountBars(
    LocalUtils.simulate(
        circuit, backendName="ibmq_quito"
    )
)
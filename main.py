from qiskit import QuantumCircuit

from qiskit_aer import AerSimulator

from qiskit.visualization import plot_histogram

simulador = AerSimulator()

qc = QuantumCircuit(1)

qc.measure_all()

qc.draw("mpl")

resultado = simulador.run(qc, shots=1000).result()

contagens = resultado.get_counts()

contagens
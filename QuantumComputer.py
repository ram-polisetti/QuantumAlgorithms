from qiskit import *
from qiskit_ibm_runtime import QiskitRuntimeService
import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram
import time

with open('ibmapi.txt', 'r') as file:
    token = file.read().strip()

QiskitRuntimeService.save_account(
    token = token,
    instance = "Practice",
    set_as_default = True,
    overwrite = True
)
service = QiskitRuntimeService()

for backend in service.backends():
    name = backend.name
    qubits = backend.num_qubits
    status = backend.status().operational
    pending_jobs = backend.status().pending_jobs
    print(f"{name:20} | Qubits: {qubits} | Operational: {status} | Pending Jobs: {pending_jobs}")


backend = service.backend("ibm_brisbane")
transpiled_qc = transpile(circuit, backend=backend)


sampler = Sampler(backend)
# need to pass a list of circuits to `sampler.run()`, even if you have only one circuit.

job = sampler.run([transpiled_qc], shots=1024)
while not job.done():
    print(f"Job is still running. Current status: {job.status()}")
    time.sleep(2)  # Wait for 10 seconds before checking again

job.wait_for_final_state()
print(f"Job completed with status: {job.status()}")

result = job.result()

bitvals = result[0].data.c

counts = bitvals.get_counts()

print(counts)

plot_histogram(counts)
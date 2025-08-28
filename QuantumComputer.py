from qiskit import *
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler
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
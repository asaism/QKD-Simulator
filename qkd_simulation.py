from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import numpy as np

def encode_message(bits, bases):
    message = []
    for i in range(len(bits)):
        qc = QuantumCircuit(1,1)
        if bases[i] == 0: # Prepare qubit in Z-basis
            if bits[i] == 0:
                pass 
            else:
                qc.x(0)
        else: # Prepare qubit in X-basis
            if bits[i] == 0:
                qc.h(0)
            else:
                qc.x(0)
                qc.h(0)
        qc.barrier()
        message.append(qc)
    return message

def measure_message(message, bases):
    measurements = []
    simulator = AerSimulator()
    for q in range(len(message)):
        if bases[q] == 0: # measuring in Z-basis
            message[q].measure(0,0)
        if bases[q] == 1: # measuring in X-basis
            message[q].h(0)
            message[q].measure(0,0)
        # Transpile the circuit for the simulator
        transpiled_circuit = transpile(message[q], simulator)
        # Run the circuit on the simulator
        job = simulator.run(transpiled_circuit, shots=1, memory=True)
        result = job.result()
        measured_bit = int(result.get_memory()[0])
        measurements.append(measured_bit)
    return measurements

def remove_garbage(a_bases, b_bases, bits):
    good_bits = []
    for q in range(len(a_bases)):
        if a_bases[q] == b_bases[q]:
            good_bits.append(bits[q])
    return good_bits

def sample_bits(bits, selection):
    sample = []
    for i in selection:
        i = np.mod(i, len(bits))
        sample.append(bits.pop(i))
    return sample

# Alice's actions
n = 100
alice_bits = np.random.randint(2, size=n)
alice_bases = np.random.randint(2, size=n)
message = encode_message(alice_bits, alice_bases)

# Bob's actions
bob_bases = np.random.randint(2, size=n)
bob_results = measure_message(message, bob_bases)

# Keep only the bits where Alice and Bob used the same basis
alice_key = remove_garbage(alice_bases, bob_bases, alice_bits)
bob_key = remove_garbage(alice_bases, bob_bases, bob_results)

# Sample bits to check for eavesdropping
sample_size = 15
bit_selection = np.random.randint(len(alice_key), size=sample_size)

alice_sample = sample_bits(alice_key, bit_selection)
bob_sample = sample_bits(bob_key, bit_selection)

print("Alice's key:", alice_key)
print("Bob's key:", bob_key)
print("Alice's sample:", alice_sample)
print("Bob's sample:", bob_sample)
print("Identical:", alice_sample == bob_sample)
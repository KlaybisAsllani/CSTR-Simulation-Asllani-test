import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def simulate_impulse_response(V, F, k):
    tau = V / (F + V * k)
    num = [1]
    den = [tau, 1]
    system = signal.TransferFunction(num, den)
    t, response = signal.impulse(system)
    plt.plot(t, response)
    plt.title('CSTR Impulse Response (Concentration)')
    plt.xlabel('Time [s]')
    plt.ylabel('Concentration')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    simulate_impulse_response(1.0, 0.5, 0.1)

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def simulate_impulse_response():
    V = 1.0
    F = 0.5
    k = 0.1

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
    simulate_impulse_response()
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def simulate_sinusoidal_response(V, F, k):
    tau = V / (F + V * k)
    num = [1]
    den = [tau, 1]
    system = signal.TransferFunction(num, den)
    t = np.linspace(0, 100, 1000)
    u = np.sin(t)
    t, response, _ = signal.lsim(system, U=u, T=t)
    plt.plot(t, response)
    plt.title('CSTR Sinusoidal Response (Concentration)')
    plt.xlabel('Time [s]')
    plt.ylabel('Concentration')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    simulate_sinusoidal_response(1.0, 0.5, 0.1)

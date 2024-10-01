import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def simulate_sinusoidal_response():
    V = 1.0  # Reactor volume (m³)
    F = 0.5  # Volumetric flow rate (m³/s)
    k = 0.1  # Reaction rate constant (1/s)

    tau = V / (F + V * k)

    # Transfer function numerator and denominator (C_A(s) / C_A0(s))
    num = [1]  # Numerator (gain = 1)
    den = [tau, 1]  # Denominator (tau s + 1)

    system = signal.TransferFunction(num, den)

    # Simulate response to a sinusoidal input
    t = np.linspace(0, 100, 1000)
    u = np.sin(t)  # Sinusoidal input
    t, response, _ = signal.lsim(system, U=u, T=t)

    plt.plot(t, response)
    plt.title('CSTR Sinusoidal Response (Concentration)')
    plt.xlabel('Time [s]')
    plt.ylabel('Concentration')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    simulate_sinusoidal_response()

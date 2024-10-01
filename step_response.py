import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def simulate_step_response():
    V = 1.0  # Reactor volume (m³)
    F = 0.5  # Volumetric flow rate (m³/s)
    k = 0.1  # Reaction rate constant (1/s)

    tau = V / (F + V * k)

    # Transfer function numerator and denominator (C_A(s) / C_A0(s))
    num = [1]  # Numerator (gain = 1)
    den = [tau, 1]  # Denominator (tau s + 1)

    system = signal.TransferFunction(num, den)

    t, response = signal.step(system)

    plt.plot(t, response)
    plt.title('CSTR Step Response (Concentration)')
    plt.xlabel('Time [s]')
    plt.ylabel('Concentration')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    simulate_step_response()

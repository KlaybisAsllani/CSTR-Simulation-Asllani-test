import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def simulate_rectangular_pulse_response():
    V = 1.0
    F = 0.5
    k = 0.1

    tau = V / (F + V * k)

    num = [1]
    den = [tau, 1]

    system = signal.TransferFunction(num, den)

    t = np.linspace(0, 100, 1000)
    u = np.zeros_like(t)
    pulse_start = 20
    pulse_end = 40
    u[(t >= pulse_start) & (t <= pulse_end)] = 1

    t, response, _ = signal.lsim(system, U=u, T=t)

    plt.plot(t, response, label='System Response')
    plt.plot(t, u, label='Rectangular Pulse Input', linestyle='--')
    plt.title('CSTR Rectangular Pulse Response (Concentration)')
    plt.xlabel('Time [s]')
    plt.ylabel('Concentration')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    simulate_rectangular_pulse_response()
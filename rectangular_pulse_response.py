import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def simulate_rectangular_pulse_response(V, F, k, pulse_start, pulse_end):
    tau = V / (F + V * k)
    num = [1]
    den = [tau, 1]
    system = signal.TransferFunction(num, den)
    t = np.linspace(0, 100, 1000)
    u = np.zeros_like(t)
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
    simulate_rectangular_pulse_response(1.0, 0.5, 0.1, 20, 40)

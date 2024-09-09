import numpy as np
import matplotlib.pyplot as plt
import control

def simulate_pid_control():
    # Define system parameters
    V = 1.0  # Reactor volume (m³)
    F = 0.5  # Volumetric flow rate (m³/s)
    k = 0.1  # Reaction rate constant (1/s)

    # Time constant
    tau = V / (F + V * k)

    # Transfer function numerator and denominator (C_A(s) / C_A0(s))
    num = [1]  # Numerator (gain = 1)
    den = [tau, 1]  # Denominator (tau s + 1)

    # Create transfer function
    system = control.TransferFunction(num, den)

    # PID controller parameters
    Kp = 1.0
    Ki = 0.1
    Kd = 0.01

    # Create PID controller
    pid = control.TransferFunction([Kd, Kp, Ki], [1, 0])

    # Closed-loop system with PID controller
    closed_loop = control.feedback(pid * system, 1)

    # Simulate the step response of the closed-loop system
    t, response = control.step_response(closed_loop)

    # Plot the result
    plt.plot(t, response)
    plt.title('CSTR Step Response with PID Control (Concentration)')
    plt.xlabel('Time [s]')
    plt.ylabel('Concentration')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    simulate_pid_control()
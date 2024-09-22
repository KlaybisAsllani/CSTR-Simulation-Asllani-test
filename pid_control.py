import numpy as np
import matplotlib.pyplot as plt
import control

def simulate_pid_control():
    V = 1.0
    F = 0.5
    k = 0.1
    tau = V / (F + V * k)
    num = [1]
    den = [tau, 1]
    system = control.TransferFunction(num, den)
    Ku = 2.0
    Tu = 10.0
    Kp = 0.6 * Ku
    Ki = 1.2 * Ku / Tu
    Kd = 3 * Ku * Tu / 40
    pid = control.TransferFunction([Kd, Kp, Ki], [1, 0])
    c_ref = 0.8
    closed_loop = control.feedback(pid * system, 1)
    t, response = control.step_response(closed_loop)
    response = response * c_ref
    plt.plot(t, response)
    plt.title('CSTR Step Response with PID Control (Concentration of Product B)')
    plt.xlabel('Time [s]')
    plt.ylabel('Concentration of Product B')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    simulate_pid_control()

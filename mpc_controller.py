import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

class HeatExchangerModel:
    def __init__(self, K, tau):
        self.K = K
        self.tau = tau
        self.T = 0  # Initial temperature
    
    def step(self, u, dt):
        # Discrete-time model using Euler's method
        T_next = (1 - dt / self.tau) * self.T + (self.K * u * dt / self.tau)
        self.T = T_next
        return self.T

class MPCController:
    def __init__(self, model, N, M, dt, Q, R):
        self.model = model
        self.N = N  # Prediction horizon
        self.M = M  # Control horizon
        self.dt = dt
        self.Q = Q  # Weight for tracking error
        self.R = R  # Weight for control effort
        self.u_prev = 0
    
    def objective_function(self, u_seq, T_ref):
        T_pred = np.zeros(self.N)
        T_pred[0] = self.model.T
        cost = 0
        
        for i in range(1, self.N):
            u = u_seq[min(i, self.M-1)]
            T_pred[i] = self.model.step(u, self.dt)
            cost += self.Q * (T_ref[i] - T_pred[i])**2 + self.R * (u - self.u_prev)**2
        
        return cost
    
    def optimize(self, T_ref):
        initial_guess = np.zeros(self.M)
        bounds = [(0, 100)] * self.M  # Bounds for control inputs
        
        result = minimize(self.objective_function, initial_guess, args=(T_ref,), bounds=bounds)
        u_opt = result.x
        self.u_prev = u_opt[0]
        return u_opt[0]

def simulate_mpc(model, controller, T_ref, simulation_time, dt):
    num_steps = int(simulation_time / dt)
    T_history = np.zeros(num_steps)
    u_history = np.zeros(num_steps)
    
    for k in range(num_steps):
        T_ref_seq = np.full(controller.N, T_ref[k])
        u_opt = controller.optimize(T_ref_seq)
        T_next = model.step(u_opt, dt)
        
        T_history[k] = T_next
        u_history[k] = u_opt
    
    return T_history, u_history

def main():
    print("Running CSTR Simulation...")
    
    print("Simulating Step Response...")
    import step_response
    step_response.simulate_step_response()
    
    print("Simulating Ramp Response...")
    import ramp_response
    ramp_response.simulate_ramp_response()
    
    print("Simulating Sinusoidal Response...")
    import sinusoidal_response
    sinusoidal_response.simulate_sinusoidal_response()

    print("Simulating PID Control...")
    import pid_control
    pid_control.simulate_pid_control()

    # Parameters
    K = 1.0
    tau = 10.0
    N = 10
    M = 5
    dt = 1.0
    Q = 1.0
    R = 0.1
    simulation_time = 100.0

    # Initial conditions
    T_initial = 20.0
    T_ref = np.linspace(20, 80, int(simulation_time / dt))

    # Create model and controller
    model = HeatExchangerModel(K, tau)
    model.T = T_initial
    controller = MPCController(model, N, M, dt, Q, R)

    # Simulate
    T_history, u_history = simulate_mpc(model, controller, T_ref, simulation_time, dt)

    # Plot results
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(np.arange(0, simulation_time, dt), T_history, label='Temperature')
    plt.plot(np.arange(0, simulation_time, dt), T_ref, 'k--', label='Reference')
    plt.xlabel('Time (s)')
    plt.ylabel('Temperature (°C)')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(np.arange(0, simulation_time, dt), u_history, label='Control Input')
    plt.xlabel('Time (s)')
    plt.ylabel('Control Input (u)')
    plt.legend()

    plt.show()

if __name__ == "__main__":
    main()
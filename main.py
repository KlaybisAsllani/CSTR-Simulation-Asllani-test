import step_response
import ramp_response
import sinusoidal_response
import pid_control
import rectangular_pulse_response
import impulse_response
import random_noise_response

def main():
    print("Running CSTR Simulation...")
    
    print("Simulating Step Response...")
    step_response.simulate_step_response()
    
    print("Simulating Ramp Response...")
    ramp_response.simulate_ramp_response()
    
    print("Simulating Sinusoidal Response...")
    sinusoidal_response.simulate_sinusoidal_response()
    
    print("Simulating PID Control...")
    pid_control.simulate_pid_control()
    
    print("Simulating Rectangular Pulse Response...")
    rectangular_pulse_response.simulate_rectangular_pulse_response()
    
    print("Simulating Impulse Response...")
    impulse_response.simulate_impulse_response()
    
    print("Simulating Random Noise Response...")
    random_noise_response.simulate_random_noise_response()

if __name__ == "__main__":
    main()

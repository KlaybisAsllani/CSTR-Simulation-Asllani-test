import step_response
import ramp_response
import sinusoidal_response
import pid_control

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
    
if __name__ == "__main__":
    main()

import step_response
import ramp_response
import sinusoidal_response
import pid_control

def main():
    print("Running CSTR Simulation...")
    
    # Step Response
    print("Simulating Step Response...")
    step_response.simulate_step_response()
    
    # Ramp Response
    print("Simulating Ramp Response...")
    ramp_response.simulate_ramp_response()
    
    # Sinusoidal Response
    print("Simulating Sinusoidal Response...")
    sinusoidal_response.simulate_sinusoidal_response()
    
    # PID Control
    print("Simulating PID Control...")
    pid_control.simulate_pid_control()

if __name__ == "__main__":
    main()
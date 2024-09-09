def calculate_time_constant(V, F, k):
    return V / (F + V * k)

if __name__ == "__main__":
    # Example usage
    V = 1.0
    F = 0.5
    k = 0.1
    tau = calculate_time_constant(V, F, k)
    print(f"Time constant: {tau}")
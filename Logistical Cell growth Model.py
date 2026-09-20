import matplotlib.pyplot as plt

# SET PARAMETERS
P = 10.0 # Initial population (e.g. 10 bacterial cells)
r = 0.01 # Growth rate constant - this is different for different organisms (e.g. E.coli has a high r value)
K = 1000000.0 # Carrying capacity (max cells the container can support)
dt = 0.1 # Change in time (e.g. 0.1 hours) - decides when the code pauses to calculate the new population number - the bigger this number, the less accurate
total_time = 3000 # Total hours to simulate

# Lists to store our data for plotting
time_points = []
population_points = []

# SIMULATION LOOP
current_time = 0.0

while current_time <= total_time:
    # Save current state
    time_points.append(current_time)
    population_points.append(P)
    
    # Calculate growth rate using the logistic differential equation
    dP_dt = r * P * (1 - (P / K))
    
    # Update population for the next small time step
    P += dP_dt * dt
    current_time += dt

# PLOT THE RESULTS
plt.figure(figsize=(8, 5))
plt.plot(time_points, population_points, label="Logistic Growth (Real-World)", color="blue", linewidth=2)
plt.axhline(y=K, color="red", linestyle="--", label="Carrying Capacity (K)") 
#axhline stands for axishorizontalline - draws single line across the graph at a height on the y axis
plt.title("Bacterial Cell Growth Simulation", fontsize=14)
plt.xlabel("Time (Hours)", fontsize=12)
plt.ylabel("Population Count (P)", fontsize=12)
plt.grid(True)
plt.legend()
plt.show()

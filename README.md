# Logistic Cell Growth Simulation

A basic Python simulation that models bacterial cell growth over time. It uses Euler's method to solve the logistic differential equation and plots the growth curve using Matplotlib.

## Overview
Unlike basic exponential growth, this model includes a carrying capacity ($K$) to simulate real-world environmental limits like restricted space and nutrients. 

The equation used is:
$$\frac{dP}{dt} = rP\left(1 - \frac{P}{K}\right)$$

* **P**: Cell population
* **r**: Growth rate constant
* **K**: Carrying capacity
* **dt**: Time step (0.1 hours)

As the population approaches $K$, growth slows down until it flattens out into an S-curve (sigmoidal curve).

## How It's Coded
I solved the equation step-by-step using **Euler's method** inside a standard loop:

```python
# Calculate growth rate using the logistic differential equation
dP_dt = r * P * (1 - (P / K))

# Update population for the next small time step
P += dP_dt * dt
current_time += dt

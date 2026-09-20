# Logistic Cell Growth Simulation

A basic Python simulation that models bacterial cell growth over time. It uses Euler's method to solve the logistic differential equation and plots the growth curve using Matplotlib.

## Overview
Unlike basic exponential growth, this model includes a carrying capacity ($K$) to simulate real-world environmental limits like restricted space and nutrients. 

The equation used is:
dP/dt = r * P * (1 - P / K)

* **P**: Cell population
* **r**: Growth rate constant
* **K**: Carrying capacity
* **dt**: Time step (0.1 hours)

As the population approaches $K$, growth slows down until it flattens out into an S-curve (sigmoidal curve).

## How It's Coded
I solved the equation step-by-step using **Euler's method** inside a standard loop:

```python
# Updating population for each time step
dP_dt = r * P * (1 - (P / K))
P += dP_dt * dt
current_time += dt

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Coefficients for the objective function (costs to minimize)
c = [25, 20]  # Costs per hour for Process 1 and Process 2

# Inequalities for the production constraints
A = [
    [-3, -5],  # Constraint for Product A (90 units minimum)
    [-6, -5]   # Constraint for Product B (120 units minimum)
]
b = [-90, -120]  # Minimum requirements for products A and B

# Bounds for the variables (non-negative production hours)
x_bounds = (0, None)  # No negative hours for Process 1
y_bounds = (0, None)  # No negative hours for Process 2

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# Extract the solution
x1, x2 = result.x  # Hours for Process 1 and Process 2

# Generate data for graphical visualization
x_vals = np.linspace(0, 40, 400)
y1_vals = (90 - 3 * x_vals) / 5  # Constraint line for Product A
y2_vals = (120 - 6 * x_vals) / 5  # Constraint line for Product B

# Plot the feasible region and constraints
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y1_vals, label='Product A Constraint (3x1 + 5x2 ≥ 90)', color='blue')
plt.plot(x_vals, y2_vals, label='Product B Constraint (6x1 + 5x2 ≥ 120)', color='green')

# Shading feasible region
plt.fill_between(x_vals, np.maximum(y1_vals, y2_vals), 40, where=(y1_vals >= 0) & (y2_vals >= 0), color='gray', alpha=0.3)

# Mark the solution point
plt.scatter(x1, x2, color='red', label=f'Optimal Solution ({x1:.2f}, {x2:.2f})')

# Labels and legend
plt.title('Feasible Region and Optimal Solution for Production Scheduling')
plt.xlabel('Hours for Process 1 (x1)')
plt.ylabel('Hours for Process 2 (x2)')
plt.xlim(0, 40)
plt.ylim(0, 40)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.grid()
plt.savefig('ODS_Aufgabe_1.png', dpi=300)

# Show the plot
plt.show()


# Display results
print(f"Optimal hours for Process 1 (x1): {x1:.2f}")
print(f"Optimal hours for Process 2 (x2): {x2:.2f}")
print(f"Minimal costs: {result.fun:.2f}€")

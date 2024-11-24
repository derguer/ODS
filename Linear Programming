import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Coefficients for the objective function (costs to minimize)
# x: Old insecticide (40% A, 35% B), y: New insecticide (15% A, 10% B)
cost_per_old = 0  # Cost for old insecticide (per 10 kg)
cost_per_new = 4  # Additional cost for new insecticide (per 10 kg)
c = [cost_per_old, cost_per_new]

# Constraints for the composition
A = [
    [0.4, 0.15],  # Percentage of toxin A
    [0.35, 0.10],  # Percentage of toxin B
    [-1, -1]  # Total mixture constraint (must equal 1)
]
b = [0.36, 0.28, -1]  # Max percentages for A, B, and total mixture

# Bounds for the variables (non-negative proportions)
x_bounds = (0, 1)  # Old insecticide
y_bounds = (0, 1)  # New insecticide

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# Extract the solution
old_insecticide, new_insecticide = result.x

# Generate data for constraints visualization
x_vals = np.linspace(0, 1, 100)
a_constraint = (0.36 - 0.4 * x_vals) / 0.15  # Toxin A constraint
b_constraint = (0.28 - 0.35 * x_vals) / 0.10  # Toxin B constraint

# Plot constraints and feasible region
plt.figure(figsize=(10, 6))
plt.plot(x_vals, a_constraint, label='Toxin A Constraint (0.4x + 0.15y ≤ 0.36)', color='blue')
plt.plot(x_vals, b_constraint, label='Toxin B Constraint (0.35x + 0.10y ≤ 0.28)', color='green')
plt.fill_between(x_vals, 0, np.minimum(a_constraint, b_constraint), where=(a_constraint >= 0) & (b_constraint >= 0),
                 color='gray', alpha=0.3, label='Feasible Region')

# Mark the optimal solution
plt.scatter(old_insecticide, new_insecticide, color='red', s=100,
            label=f'Optimal Solution\n(Old: {old_insecticide:.2f}, New: {new_insecticide:.2f})')

# Labels, title, and legend
plt.title('Feasible Region and Optimal Solution for Insecticide Mixture', fontsize=14)
plt.xlabel('Proportion of Old Insecticide (x)', fontsize=12)
plt.ylabel('Proportion of New Insecticide (y)', fontsize=12)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend(fontsize=10)
plt.grid(alpha=0.4)
plt.savefig('ODS_Aufagbe_3.png',dpi=300)

# Show the plot
plt.show()

# Display results
print(f"Optimal proportion of old insecticide: {old_insecticide:.2f}")
print(f"Optimal proportion of new insecticide: {new_insecticide:.2f}")
print(f"Minimized cost per 10 kg: {result.fun:.2f}€")

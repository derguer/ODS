
#Update of the format

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Coefficients for the objective function (profit maximization)
# Muffins: 0.50€/dozen, Brownies: 0.80€/box
profit_per_muffin = 0.50
profit_per_brownie = 0.80
c = [-profit_per_muffin, -profit_per_brownie]  # Negative for maximization

# Constraints for ingredients
# Muffins: 750g Mehl, 150g Zucker; Brownies: 570g Mehl, 450g Zucker
# Maximal 81 Pfund Mehl (81,000g) and 51 Pfund Zucker (51,000g)
A = [
    [750, 570],  # Mehl constraint
    [150, 450]   # Zucker constraint
]
b = [81000, 51000]  # Max available Mehl and Zucker

# Bounds for the variables (non-negative amounts of muffins and brownies)
x_bounds = (0, None)  # Muffins
y_bounds = (0, None)  # Brownies

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# Extract the solution
muffins, brownies = result.x

# Generate data for constraints visualization
x_vals = np.linspace(0, 120, 400)  # Generate range for Muffins (x)
mehl_constraint = (81000 - 750 * x_vals) / 570  # Mehl constraint line
zucker_constraint = (51000 - 150 * x_vals) / 450  # Zucker constraint line

# Plot constraints and feasible region
plt.figure(figsize=(10, 6))
plt.plot(x_vals, mehl_constraint, label='Mehl Constraint (750x + 570y ≤ 81000)', color='blue')
plt.plot(x_vals, zucker_constraint, label='Zucker Constraint (150x + 450y ≤ 51000)', color='green')
plt.fill_between(x_vals, 0, np.minimum(mehl_constraint, zucker_constraint), where=(mehl_constraint >= 0) & (zucker_constraint >= 0),
                 color='gray', alpha=0.3, label='Feasible Region')

# Mark the optimal solution
plt.scatter(muffins, brownies, color='red', s=100,
            label=f'Optimal Solution\n(Muffins: {muffins:.2f}, Brownies: {brownies:.2f})')

# Labels, title, and legend
plt.title('Feasible Region and Optimal Solution for Bakery Production', fontsize=14)
plt.xlabel('Dozens of Muffins (x)', fontsize=12)
plt.ylabel('Boxes of Brownies (y)', fontsize=12)
plt.xlim(0, 120)
plt.ylim(0, 120)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend(fontsize=10)
plt.grid(alpha=0.4)
plt.savefig('ODS_Aufgabe_2.4.png', dpi=300)

# Show the plot
plt.show()

# Display results
print(f"Optimal number of dozens of muffins: {muffins:.2f}")
print(f"Optimal number of boxes of brownies: {brownies:.2f}")
print(f"Maximized profit: {result.fun * -1:.2f}€")

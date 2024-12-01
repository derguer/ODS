# ODS Aufgabe 7 Parztikelschwarm- und Genetischer Algorythmus

import pyswarms as ps
import numpy as np

# Fitnessfunktion
def fitness_function(x):
    return 0.26 * (x[:, 0]**2 + x[:, 1]**2) - 0.48 * x[:, 0] * x[:, 1]

# Parameter
bounds = (-5, 5)
options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}

# Optimierung
optimizer = ps.single.GlobalBestPSO(n_particles=50, dimensions=2, options=options, bounds=bounds)
best_cost, best_pos = optimizer.optimize(fitness_function, iters=100)
print("Bestes Ergebnis:", best_cost, "Position:", best_pos)

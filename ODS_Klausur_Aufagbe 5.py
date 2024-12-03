import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Zielfunktionskoeffizienten
c = [8, 17, 15, 10, 13, 21, 22]  # Kostenkoeffizienten

# Nebenbedingungen
A = [
    [1, 1, 1, 0, 0, 0, 0],  # Lager 1 Kapazität
    [0, 0, 0, 1, 1, 1, 1],  # Lager 2 Kapazität
    [0, 0, 0, 1, 0, 0, 0],  # y_{21} Kapazität
]
b = [100, 100, 20]  # Kapazitätsgrenzen

# Gleichungen für Nachfrage
A_eq = [
    [1, 0, 0, 1, 1, 0, 0],  # Geschäft 1 Nachfrage
    [0, 1, 0, 0, 0, 1, 0],  # Geschäft 2 Nachfrage
    [0, 0, 1, 0, 0, 0, 1],  # Geschäft 3 Nachfrage
]
b_eq = [50, 50, 50]  # Nachfrage

# Variablenbeschränkungen (alle Variablen >= 0)
bounds = [(0, None) for _ in range(len(c))]

# Optimierung durchführen
result = linprog(c, A_ub=A, b_ub=b, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

# Optimalen Punkt extrahieren
if result.success:
    x_optimal = result.x[:2]  # Werte für x11 und x12
    optimal_value = result.fun

# Daten für grafische Darstellung
x_vals = np.linspace(0, 100, 500)
y1_constraint = 100 - x_vals  # Lager 1 Kapazität
y2_constraint = 50 - x_vals  # Geschäft 2 Nachfrage

# Zeichnen der Nebenbedingungen und zulässige Region
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y1_constraint, label="Kapazität Lager 1 (x11 + x12 ≤ 100)", color='blue')
plt.axhline(50, color='green', linestyle='--', label="Nachfrage Geschäft 2 (x12 ≤ 50)")
plt.axvline(50, color='red', linestyle='--', label="Nachfrage Geschäft 1 (x11 ≤ 50)")

# Feasible Region schattieren
plt.fill_between(x_vals, 0, np.minimum(y1_constraint, 50), where=(x_vals <= 50),
                 color='gray', alpha=0.3, label="Zulässige Region")

# Optimale Lösung markieren
plt.scatter(x_optimal[0], x_optimal[1], color='purple', s=100,
            label=f"Optimale Lösung\n(x11: {x_optimal[0]:.2f}, x12: {x_optimal[1]:.2f})")

# Beschriftungen und Layout
plt.title('Zulässige Region und Optimale Lösung für Transportproblem', fontsize=14)
plt.xlabel('Transport von Lager 1 zu Geschäft 1 (x11)', fontsize=12)
plt.ylabel('Transport von Lager 1 zu Geschäft 2 (x12)', fontsize=12)
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend(fontsize=10)
plt.grid(alpha=0.4)
plt.savefig('Transportproblem_Grafik.png', dpi=300)
plt.show()

# Ergebnis anzeigen
if result.success:
    print(f"Optimale Transportmengen:")
    print(f"Von Lager 1 zu Geschäft 1 (x11): {x_optimal[0]:.2f}")
    print(f"Von Lager 1 zu Geschäft 2 (x12): {x_optimal[1]:.2f}")
    print(f"Minimalen Transportkosten: {optimal_value:.2f} €")
else:
    print("Keine Lösung gefunden!")

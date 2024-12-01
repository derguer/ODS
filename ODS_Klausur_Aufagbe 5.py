
# ODS Aufgabe 5: Lösung in Python

from scipy.optimize import linprog

# Zielfunktion (Transportkosten)
c = [8, 17, 15, 10, 21, 22]  # Transportkosten

# Nebenbedingungen
A = [
    [1, 1, 1, 0, 0, 0],  # Lager 1 Kapazität
    [0, 0, 0, 1, 1, 1],  # Lager 2 Kapazität
    [1, 0, 0, 1, 0, 0],  # Geschäft 1 Bedarf
    [0, 1, 0, 0, 1, 0],  # Geschäft 2 Bedarf
    [0, 0, 1, 0, 0, 1]   # Geschäft 3 Bedarf
]
b = [100, 100, 50, 50, 50]  # Kapazitäten und Bedarfe

# Optimierung
result = linprog(c, A_eq=A, b_eq=b, method='highs')
print("Optimale Lösung:", result.x)
print("Minimale Kosten:", result.fun)

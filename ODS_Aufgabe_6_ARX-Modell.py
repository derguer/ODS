# ODS Aufgabe 6: ARX-Modell

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

# Daten einlesen
u = pd.read_csv('u.csv')  # Eingangsgrößen
y = pd.read_csv('y.csv')  # Ausgangsgrößen

# 1. Glättung
u_smooth = u.rolling(window=7, center=True).mean()
y_smooth = y.rolling(window=7, center=True).mean()

# 2. Skalierung
scaler_u = StandardScaler()
scaler_y = StandardScaler()
u_scaled = scaler_u.fit_transform(u_smooth.dropna())
y_scaled = scaler_y.fit_transform(y_smooth.dropna())

# 3. Zeitliche Verschiebung
u_shifted = np.roll(u_scaled, 4, axis=0)
y_shifted = y_scaled[4:]

# 4. ARX-Modell (hier einfach linear)
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(u_shifted, y_shifted)

# 5. Evaluierung
y_pred = model.predict(u_shifted)
rmse = mean_squared_error(y_shifted, y_pred, squared=False)
print("RMSE:", rmse)

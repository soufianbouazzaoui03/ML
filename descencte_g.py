import numpy as np


surface = np.array([])
prix = np.array([])

theta_0 = 0
theta_1 = 0

alpa = 0.00001
epochs = 1000

m = len(surface)

i = 0

while i < m:
    predict = theta_0 + theta_1 * surface[i]
    errors = predict - prix

d_theta_0 = (1/m) * np.sum(errors)
d_theta_1 = (1/m) * np.sum(errors * surface)

theta_0 -= alpha *d_theta_0
theta_1 -= alpha * d_theta_1 

 if epoch % 1000 == 0:
 cost = (1 / (2 * m)) * np.sum(errors**2)
 print(f"Epoch {epoch}: Coût = {cost:.2f}")
# Résultats finaux
print(f"Paramètres optimisés : theta_0 = {theta_0:.2f},
theta_1 = {theta_1:.2f}")
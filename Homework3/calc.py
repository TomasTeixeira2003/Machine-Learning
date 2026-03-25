import numpy as np

# Data points and targets
X = np.array([[0.7, -0.3], [0.4, 0.5], [-0.2, 0.8], [-0.4, 0.3]])
y = np.array([0.8, 0.6, 0.3, 0.3])

# Centers
c1 = np.array([0, 0])
c2 = np.array([1, -1])
c3 = np.array([-1, 1])

# Compute RBF features for each data point
phi0 = np.ones(X.shape[0])
phi1 = np.exp(-np.linalg.norm(X - c1, axis=1)**2 / 2)
phi2 = np.exp(-np.linalg.norm(X - c2, axis=1)**2 / 2)
phi3 = np.exp(-np.linalg.norm(X - c3, axis=1)**2 / 2)

# Create the design matrix Φ
Φ = np.column_stack((phi0, phi1, phi2, phi3))

# Regularization parameter
λ = 0.1

# Calculate the weights using Ridge regression formula
I = np.identity(4)
w = np.linalg.inv(Φ.T @ Φ + λ * I) @ Φ.T @ y

# Print the weights
#print(w)

# Make predictions on the training data
y_pred = Φ @ w

# Calculate residuals
residuals = y - y_pred

# Calculate RMSE
rmse = np.sqrt(np.mean(residuals**2))

# Print the RMSE
print("Training RMSE:", rmse)


    
    
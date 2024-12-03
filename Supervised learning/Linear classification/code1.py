import numpy as np
from sklearn.linear_model import LogisticRegression

# Dataset
x = [1, 3, 5, 7, 9]
y = [3, 10, 8, 19, 16]
z = [-1, 1, -1, 1, -1]  # Classification

# Prepare the data for the model
X = np.array(list(zip(x, y)))  # Feature matrix
z = np.array(z)  # Targets

# Create and train a Logistic Regression model
model = LogisticRegression()
model.fit(X, z)

# Get the coefficients
coef = model.coef_[0]
intercept = model.intercept_[0]

# Calculate the slope and intercept of the decision boundary
slope = -coef[0] / coef[1]
intercept_line = -intercept / coef[1]

print(f"Slope: {slope}")
print(f"Intercept: {intercept_line}")

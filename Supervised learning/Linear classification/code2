import numpy as np
import matplotlib.pyplot as plt
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

# Plotting decision boundary
plt.figure(figsize=(8, 6))

# Scatter plot
for i in range(len(x)):
    if z[i] == 1:
        plt.scatter(x[i], y[i], color='red', s=100)  # Red for class 1
    else:
        plt.scatter(x[i], y[i], color='blue', s=100) # Blue for class -1

# Define bounds
xmin, xmax = min(x) - 1, max(x) + 1
ymin, ymax = min(y) - 1, max(y) + 1

# Create grid to evaluate model
xx, yy = np.meshgrid(np.arange(xmin, xmax, 0.1), np.arange(ymin, ymax, 0.1))

# Decision boundary
Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Plot decision boundary
plt.contourf(xx, yy, Z, alpha=0.3)
plt.title('Scatter Plot with Decision Boundary')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()

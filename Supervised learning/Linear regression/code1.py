import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Dataset
x = np.array([1, 3, 5, 7, 9]).reshape(-1, 1)  # Reshape for scikit-learn
y = np.array([3, 10, 8, 19, 16])

# Create and fit the model
model = LinearRegression()
model.fit(x, y)

# Get the slope and intercept
slope = model.coef_[0]
intercept = model.intercept_

print(f"Slope: {slope}, Intercept: {intercept}")

# Generate the regression line
regression_line = [slope * xx + intercept for xx in x]

# Plot the graph
plt.figure(figsize=(5, 5))
plt.scatter(x, y, marker='o', label='Data points')
plt.plot(x, regression_line, color='red', label='Regression line')
plt.title('Linear Regression Fit')
plt.xlabel('x values')
plt.ylabel('y values')
plt.grid(True)
plt.xticks(x.flatten())
plt.yticks(range(0, 30, 5))
plt.legend()

# Display the graph
plt.show()

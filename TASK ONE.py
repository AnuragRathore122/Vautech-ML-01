import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Generate dataset
np.random.seed(0)
X = np.linspace(-3, 3, 50).reshape(-1, 1)
y = X**2 + np.random.randn(50, 1)

# Polynomial degrees
degrees = [1, 2, 10]

plt.scatter(X, y, color='black', label='Data')

for degree in degrees:
    poly = PolynomialFeatures(degree)
    X_poly = poly.fit_transform(X)

    model = LinearRegression()
    model.fit(X_poly, y)

    y_pred = model.predict(X_poly)
    plt.plot(X, y_pred, label=f'Degree {degree}')

plt.legend()
plt.xlabel("X")
plt.ylabel("y")
plt.title("Bias–Variance Tradeoff")
plt.show()

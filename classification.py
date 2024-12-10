import numpy as np

data = np.array([
    [80, 85, 1],
    [60, 70, 0],
    [90, 88, 1],
    [65, 60, 0],
    [75, 80, 1]
])

m, n = X.shape  # Number of samples (m) and features (n)
X = np.hstack((np.ones((m, 1)), X))  # Add bias term (x0 = 1)
theta = np.zeros(n + 1)  # Initialize weights to zero

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def compute_cost(X, y, theta):
    m = len(y)
    h = sigmoid(np.dot(X, theta))
    cost = -(1 / m) * np.sum(y * np.log(h) + (1 - y) * np.log(1 - h))
    return cost

def gradient_descent(X, y, theta, alpha, iterations):
    m = len(y)
    for _ in range(iterations):
        h = sigmoid(np.dot(X, theta))
        gradient = (1 / m) * np.dot(X.T, (h - y))
        theta -= alpha * gradient
    return theta

alpha = 0.01  # Learning rate
iterations = 1000  # Number of iterations
theta = gradient_descent(X, y, theta, alpha, iterations)


def predict(X, theta):
    probabilities = sigmoid(np.dot(X, theta))
    return [1 if p >= 0.5 else 0 for p in probabilities]


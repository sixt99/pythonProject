import numpy as np


def function(x, y):
    return (x - 3) ** 2 + y ** 2


def derivative(x, y):
    return [2 * (x - 3), 2 * y]


minimum = [20, 3]
lam = 0.9
for i in range(100):
    print(minimum)
    minimum = minimum - np.multiply(lam, derivative(minimum[0], minimum[1]))

print(minimum)

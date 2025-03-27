import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Task 1: Basic Plotting
x = np.linspace(-10, 10, 400)
y = x**2 - 4*x + 4
plt.figure()
plt.plot(x, y, label="$f(x) = x^2 - 4x + 4$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Quadratic Function Plot")
plt.legend()
plt.grid()
plt.show()

# Task 2: Sine and Cosine Plot
x = np.linspace(0, 2*np.pi, 400)
plt.figure()
plt.plot(x, np.sin(x), linestyle='-', color='b', label="$\sin(x)$")
plt.plot(x, np.cos(x), linestyle='--', color='r', label="$\cos(x)$")
plt.xlabel("x")
plt.ylabel("Value")
plt.title("Sine and Cosine Functions")
plt.legend()
plt.grid()
plt.show()

# Task 3: Subplots
x = np.linspace(-2, 2, 400)
x_positive = np.linspace(0, 2, 400)
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
axs[0, 0].plot(x, x**3, 'g')
axs[0, 0].set_title("$f(x) = x^3$")
axs[0, 1].plot(x, np.sin(x), 'b')
axs[0, 1].set_title("$f(x) = \sin(x)$")
axs[1, 0].plot(x, np.exp(x), 'r')
axs[1, 0].set_title("$f(x) = e^x$")
axs[1, 1].plot(x_positive, np.log(x_positive + 1), 'purple')
axs[1, 1].set_title("$f(x) = \log(x+1)$")
for ax in axs.flat:
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.grid()
plt.tight_layout()
plt.show()

# Task 4: Scatter Plot
x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)
plt.figure()
plt.scatter(x, y, c=np.random.rand(100), marker='o', edgecolors='black')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Random Scatter Plot")
plt.grid()
plt.show()

# Task 5: Histogram
data = np.random.normal(0, 1, 1000)
plt.figure()
plt.hist(data, bins=30, alpha=0.7, color='blue', edgecolor='black')
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram of Normally Distributed Data")
plt.show()

# Task 6: 3D Plotting
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = np.cos(X**2 + Y**2)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis')
plt.colorbar(surf)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("f(X, Y)")
ax.set_title("3D Surface Plot")
plt.show()

# Task 7: Bar Chart
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [200, 150, 250, 175, 225]
plt.figure()
plt.bar(products, sales, color=['blue', 'red', 'green', 'orange', 'purple'])
plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Sales Data of Products")
plt.show()

# Task 8: Stacked Bar Chart
time_periods = ['T1', 'T2', 'T3', 'T4']
category_A = [3, 5, 2, 8]
category_B = [4, 6, 3, 7]
category_C = [5, 3, 4, 6]
plt.figure()
plt.bar(time_periods, category_A, label='Category A')
plt.bar(time_periods, category_B, bottom=category_A, label='Category B')
plt.bar(time_periods, category_C, bottom=np.array(category_A) + np.array(category_B), label='Category C')
plt.xlabel("Time Periods")
plt.ylabel("Values")
plt.title("Stacked Bar Chart")
plt.legend()
plt.show()

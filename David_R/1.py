import numpy as np
import matplotlib.pyplot as plt

# Generate random data
x = np.linspace(0, 10, 100)
y = np.random.normal(0, 1, 100) + np.sin(x)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', label='Random Data')
plt.scatter(x, y, color='red', alpha=0.2)

# Customize the plot
plt.title('Random Data with Sine Wave Trend')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# Show the plot
plt.show()

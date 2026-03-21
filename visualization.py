# Import required libraries
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create epochs
epochs = list(range(1, 11))

# Step 2: Generate synthetic loss values
np.random.seed(42)
loss = np.linspace(1.0, 0.2, 10) + np.random.normal(0, 0.05, 10)

# -------------------------------
# 1. Line Plot (Loss vs Epoch)
# -------------------------------
plt.figure(figsize=(8, 5))
plt.plot(epochs, loss, marker='o')
plt.title("Loss vs Epoch")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.grid(True)
plt.show()

# -------------------------------
# 2. Scatter Plot (Epoch vs Loss)
# -------------------------------
plt.figure(figsize=(8, 5))
plt.scatter(epochs, loss)
plt.title("Scatter Plot: Epoch vs Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.grid(True)
plt.show()

# -------------------------------
# 3. Bar Chart (Model Accuracy Comparison)
# -------------------------------
models = ["Model A", "Model B", "Model C"]
accuracy = [85, 90, 88]

plt.figure(figsize=(8, 5))
plt.bar(models, accuracy)
plt.title("Model Accuracy Comparison")
plt.xlabel("Models")
plt.ylabel("Accuracy (%)")
plt.grid(axis='y')
plt.show()
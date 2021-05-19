import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

data = pd.read_csv("Book1.csv")
print(data.head())

height = np.array(data["height(cm)"])
print(height)

print("Mean of heights = ", height.mean())
print("standard Deviation of height = ", height.std())
print("minimum height = ", height.min())
print("Maximum height = ", height.max())
print("25th percentile = ", np.percentile(height, 25))
print("Median = ", np.median(height))
print("75th percentile = ", np.percentile(height, 75))

sns.set()
plt.hist(height)
plt.title("Height Distribution Of Presidents of USA")
plt.xlabel("height(cm)")
plt.ylabel("number")
plt.show()

from sklearn.datasets import fetch_california_housing
import pandas as pd
import matplotlib.pyplot as plt
housing = fetch_california_housing(as_frame=True)
df = housing.frame
plt.figure(figsize=(10, 6))
df.boxplot()
plt.xticks(rotation=90)
plt.title("California Housing Dataset Boxplot")
plt.tight_layout()
plt.show()

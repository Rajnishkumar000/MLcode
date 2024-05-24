import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a DataFrame with random data
np.random.seed(42)
data = {
    'A': np.random.randn(100),
    'B': np.random.randn(100),
    'C': np.random.randn(100),
    'D': np.random.randn(100)
}
df = pd.DataFrame(data)
print(df.head())

# Create a pair plot
sns.pairplot(df)
plt.show()

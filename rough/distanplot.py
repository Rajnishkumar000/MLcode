import seaborn as sns
import matplotlib.pyplot as plt

# Sample data (replace this with your own data)
data = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,9,9,9,9,9,9,9,9,9,9,9]

# Create a distribution plot
# sns.displot(data, kde=True)  # kde=True for Kernel Density Estimation
sns.displot(data)  # kde=True for Kernel Density Estimation
plt.title('Distribution Plot')
plt.xlabel('Values')
plt.ylabel('Density')
plt.show()

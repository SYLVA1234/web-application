import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
np.random.seed(0)
dates = pd.date_range('20220101', periods=100)
data = pd.DataFrame(np.random.randn(100, 4), index=dates, columns=list('ABCD'))

# Add a new column with cumulative sum of column 'A'
data['cumulative_sum_A'] = data['A'].cumsum()

# Print the first few rows of the data
print("First few rows of the data:")
print(data.head())

# Summary statistics
print("\nSummary statistics of the data:")
print(data.describe())

# Plotting
plt.figure(figsize=(10, 5))
data['A'].plot(label='Column A')
data['B'].plot(label='Column B')
plt.title('Line Plot of Columns A and B')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()

# Scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(data['C'], data['D'])
plt.title('Scatter Plot of Columns C and D')
plt.xlabel('C')
plt.ylabel('D')
plt.grid(True)
plt.show()

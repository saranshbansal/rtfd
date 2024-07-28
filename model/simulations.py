import matplotlib.pyplot as plt
import pandas as pd

# Simulated data
data_length = 100  # Number of data points
data = {
    'date': pd.date_range(start='2024-01-01', periods=data_length, freq='D'),
    'frauds': [5, 7, 6, 3, 8, 4, 2, 9, 3, 1, 0, 2, 6, 3, 1, 5, 4, 3, 6, 5, 7, 2, 3, 1, 0, 4, 2, 3, 5, 7] * (
            data_length // 30 + 1),
    'false_positives': [1, 0, 2, 1, 3, 2, 1, 4, 1, 0, 1, 0, 3, 1, 0, 2, 1, 0, 1, 3, 0, 1, 2, 1, 3, 0, 1, 2, 0, 1] * (
            data_length // 30 + 1),
    'legitimate': [50, 48, 47, 49, 52, 50, 51, 49, 50, 52, 53, 51, 49, 50, 51, 49, 48, 52, 50, 49, 51, 50, 52, 49, 50,
                   51, 49, 50, 52, 48] * (data_length // 30 + 1)
}

# Truncate lists to the length of 'date'
data['frauds'] = data['frauds'][:data_length]
data['false_positives'] = data['false_positives'][:data_length]
data['legitimate'] = data['legitimate'][:data_length]

# Create DataFrame
df = pd.DataFrame(data)

# Plotting
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(df['date'], df['frauds'], label='Frauds', color='red')
ax.plot(df['date'], df['false_positives'], label='False Positives', color='orange')
ax.plot(df['date'], df['legitimate'], label='Legitimate Transactions', color='green')

# Adding title and labels
ax.set_title('Transactions Timeline')
ax.set_xlabel('Date')
ax.set_ylabel('Number of Transactions')
ax.legend()

# Formatting plot
plt.grid()
plt.xticks(rotation=45)
plt.tight_layout()

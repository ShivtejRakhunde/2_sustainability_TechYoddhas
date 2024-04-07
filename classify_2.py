import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
# Read the datas
df = pd.read_excel('grid_orig.xlsx')
# # Update stability column based on power1, power2, and power3 values
# df['stability'] = df.apply(lambda row: 'unstable' if row['power1'] == 0 and row['power2'] == 0 and row['power3'] == 0 else row['stability'], axis=1)

# # Write the updated dataset back to CSV
# df.to_excel('grid_orig.xlsx', index=False)


# Handle missing values
df.fillna(method='ffill', inplace=True)  # Forward fill missing values

# Filtering out erroneous values
df = df[df['date'] != "date"]

# Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y %H:%M')

# Extract month and hour from the datetime column
df['Month'] = df['date'].dt.month
df['Hour'] = df['date'].dt.hour


stability_counts = df['stability'].value_counts()

# Calculate the percentage of 'stable' and 'unstable' entries
percentage_stable = (stability_counts['stable'] / len(df)) * 100
percentage_unstable = (stability_counts['unstable'] / len(df)) * 100

print("Percentage of 'stable' entries:", percentage_stable)
print("Percentage of 'unstable' entries:", percentage_unstable)


# Filter data for one day
one_day_df = df[df['Month'] == 1]  # Assuming you want data for January, you can change this as needed
# Define a custom color palette with distinct colors for stability classes
# Define a list of colors for different lines
line_colors = ['blue', 'green', 'red','yellow','black','orange']  # You can customize the colors as needed

# Plotting time series for selected variables with stability as the hue for one day on an hourly basis
plt.figure(figsize=(12, 8))
sns.lineplot(x='Hour', y='power1', hue='stability', data=one_day_df, palette=line_colors, ci=None, label='Power 1')
sns.lineplot(x='Hour', y='power2', hue='stability', data=one_day_df, palette=line_colors, ci=None, label='Power 2')
sns.lineplot(x='Hour', y='power3', hue='stability', data=one_day_df, palette=line_colors, ci=None, label='Power 3')
plt.xlabel('Hour of the Day')
plt.ylabel('Power')
plt.title('Power Generation Trends Over Hours of the Day with Stability (One Day)')
plt.legend(title='Stability')
plt.show()
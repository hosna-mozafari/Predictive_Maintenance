import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (you can modify the path if needed)
data_path = r"D:\Predictive_Maintenance\data\train_FD002.txt"
df = pd.read_csv(data_path, sep="\s+", header=None)

# Define column names and assign them to the dataframe
column_names = [
    "unit_number", "time_in_cycles", "operational_setting_1", "operational_setting_2", 
    "operational_setting_3", "sensor_1", "sensor_2", "sensor_3", "sensor_4", 
    "sensor_5", "sensor_6", "sensor_7", "sensor_8", "sensor_9", "sensor_10", 
    "sensor_11", "sensor_12", "sensor_13", "sensor_14", "sensor_15", "sensor_16", 
    "sensor_17", "sensor_18", "sensor_19", "sensor_20", "sensor_21"
]
df.columns = column_names

# Calculate the RUL (Remaining Useful Life)
max_cycles = df.groupby('unit_number')['time_in_cycles'].max()
df['RUL'] = df['unit_number'].map(max_cycles) - df['time_in_cycles']

# Display first few rows to check if RUL was calculated correctly
print(df.head())

# Plot histogram of the 'RUL' column
plt.figure(figsize=(10, 6))
plt.hist(df['RUL'], bins=30, color='skyblue', edgecolor='black')
plt.title('Histogram of Remaining Useful Life (RUL)')
plt.xlabel('Remaining Useful Life (RUL)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


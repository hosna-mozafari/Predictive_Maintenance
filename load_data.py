import pandas as pd

# Define the dataset path
data_path = r"D:\Predictive_Maintenance\data\train_FD001.txt"  # Use raw string for Windows path

# Read the dataset, assuming space-separated values (adjust delimiter if needed)
df = pd.read_csv(data_path, sep="\s+", header=None)

# Display the first few rows to understand the structure

# Display dataset information


# Define column names
column_names = [
    "unit", "time_in_cycles", "operational_setting_1", "operational_setting_2", "operational_setting_3",
    "sensor_1", "sensor_2", "sensor_3", "sensor_4", "sensor_5", "sensor_6", "sensor_7", "sensor_8", 
    "sensor_9", "sensor_10", "sensor_11", "sensor_12", "sensor_13", "sensor_14", "sensor_15",
    "sensor_16", "sensor_17", "sensor_18", "sensor_19", "sensor_20", "sensor_21"
]

# Assign new column names
df.columns = column_names

# Print updated dataframe

# Define column names based on NASA dataset documentation
column_names = [
    "unit_number", "time_in_cycles", "operational_setting_1", "operational_setting_2", 
    "operational_setting_3", "sensor_1", "sensor_2", "sensor_3", "sensor_4", 
    "sensor_5", "sensor_6", "sensor_7", "sensor_8", "sensor_9", "sensor_10", 
    "sensor_11", "sensor_12", "sensor_13", "sensor_14", "sensor_15", "sensor_16", 
    "sensor_17", "sensor_18", "sensor_19", "sensor_20", "sensor_21"
]

# Apply new column names
df.columns = column_names

# Display first few rows to verify
print(df.head())
print("\nDataset Info:")
print(df.info())  # Shows column types and missing valuesprint("\nDataset Info:")
print(df.info())  # Shows column types and missing values

# Display basic statistics
print("\nBasic Statistics:")
print(df.describe())  # Summary of numerical columns
import pandas as pd

# Define the dataset path
data_path = r"D:\Predictive_Maintenance\data\train_FD002.txt"

# Read the dataset, assuming space-separated values
df = pd.read_csv(data_path, sep="\s+", header=None)

# Define column names (based on NASA dataset documentation)
column_names = [
    "unit_number", "time_in_cycles", "operational_setting_1", "operational_setting_2", 
    "operational_setting_3", "sensor_1", "sensor_2", "sensor_3", "sensor_4", 
    "sensor_5", "sensor_6", "sensor_7", "sensor_8", "sensor_9", "sensor_10", 
    "sensor_11", "sensor_12", "sensor_13", "sensor_14", "sensor_15", "sensor_16", 
    "sensor_17", "sensor_18", "sensor_19", "sensor_20", "sensor_21"
]
df.columns = column_names

# ----- EDA -----
print("✅ First 5 Rows:")
print(df.head())

print("\n📋 Dataset Info:")
print(df.info())

print("\n🔍 Missing Values Per Column:")
print(df.isnull().sum())

print("\n📊 Summary Statistics:")
print(df.describe())


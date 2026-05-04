import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("Benchmark/Datasets/Labeled/Nominal/1773251393.csv")

# Ensure timestamp is treated properly (optional but recommended)
# df["metric_timestamp"] = pd.to_datetime(df["metric_timestamp"])

# Set timestamp as index (optional but makes plotting easier)
df = df.set_index("metric_timestamp")

# Keep only sensor columns (exclude timestamp already handled)
sensor_df = df.copy()

# Select only columns that contain missing values
cols_with_na = sensor_df.columns[sensor_df.isna().any()]

filtered = sensor_df[cols_with_na]

# Plot
plt.figure(figsize=(12, 6))

for col in filtered.columns:
    plt.plot(filtered.index, filtered[col], label=col)

plt.legend()
plt.title("Sensors with Missing Values")
plt.xlabel("Time")
plt.ylabel("Sensor value")
plt.tight_layout()
plt.show()
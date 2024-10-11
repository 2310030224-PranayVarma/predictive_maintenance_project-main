import pandas as pd
import numpy as np

# Set the random seed for reproducibility
np.random.seed(42)

# Define the number of samples
num_samples = 1000

# Generate Machine IDs
machine_ids = [f'Machine_{i+1}' for i in range(num_samples)]

# Generate random values for other features
temperature = np.random.uniform(20, 100, num_samples)  # Temperature between 20 and 100
pressure = np.random.uniform(1, 10, num_samples)       # Pressure between 1 and 10
vibration = np.random.uniform(0, 10, num_samples)       # Vibration between 0 and 10
power = np.random.uniform(0, 100, num_samples)          # Power between 0 and 100
hours_since_last_maintenance = np.random.randint(1, 200, num_samples)  # Hours since last maintenance between 1 and 200

# Define a condition for generating failures
# Let's say that failures happen more often at higher temperatures and longer hours since last maintenance.
failure_condition = (temperature > 80) & (hours_since_last_maintenance > 150)

# Generate failures: only a small percentage will actually fail
failures = np.where(failure_condition & (np.random.rand(num_samples) < 0.2), 1, 0)  # 20% of high-risk cases will fail
# Alternatively, for controlled distribution, you can define a lower ratio:
# failures = np.random.choice([0, 1], size=num_samples, p=[0.9, 0.1])  # 10% failure rate

# Create a DataFrame
data = pd.DataFrame({
    'Machine_ID': machine_ids,
    'Temperature': temperature,
    'Pressure': pressure,
    'Vibration': vibration,
    'Power': power,
    'Hours_Since_Last_Maintenance': hours_since_last_maintenance,
    'Failures': failures
})

# Save the DataFrame to an Excel file
output_file = 'test/machine_data_large.xlsx'
data.to_excel(output_file, index=False)

print(f"Dataset with {num_samples} rows has been generated and saved to {output_file}.")

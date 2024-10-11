import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Parameters for the dataset
num_records = 1000  # Number of records
machine_ids = [f'Machine_{i}' for i in range(1, 101)]  # 100 unique machine IDs

# Generate random data
data = {
    'Machine_ID': np.random.choice(machine_ids, num_records),
    'Temperature': np.random.uniform(60, 90, num_records),  # Random temperature between 60 and 90
    'Pressure': np.random.uniform(25, 35, num_records),      # Random pressure between 25 and 35
    'Vibration': np.random.uniform(0.5, 2.0, num_records),    # Random vibration between 0.5 and 2.0
    'Power': np.random.uniform(180, 350, num_records),        # Random power between 180 and 350
    'Hours_Since_Last_Maintenance': np.random.randint(0, 500, num_records)  # Random hours since last maintenance
}

# Create a DataFrame
df = pd.DataFrame(data)

# Introduce random failures based on some conditions for testing
# For simplicity, let's say if temperature > 85 and hours since last maintenance > 100, it will fail
df['Failures'] = np.where((df['Temperature'] > 85) & (df['Hours_Since_Last_Maintenance'] > 100), 1, 0)

# Save the DataFrame to an Excel file
test_dataset_path = 'test/test_data.xlsx'
df.to_excel(test_dataset_path, index=False)

test_dataset_path

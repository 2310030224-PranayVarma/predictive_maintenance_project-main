import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Number of samples
num_samples = 100

# Generate synthetic data
data = {
    'Machine_ID': [f'Machine_{i}' for i in range(1, num_samples + 1)],
    'Temperature': np.random.uniform(20, 100, num_samples),  # Temperature between 20 and 100 degrees
    'Pressure': np.random.uniform(10, 50, num_samples),  # Pressure between 10 and 50 units
    'Vibration': np.random.uniform(0, 10, num_samples),  # Vibration level between 0 and 10 units
    'Power': np.random.uniform(50, 200, num_samples),  # Power consumption between 50 and 200 units
    'Hours_Since_Last_Maintenance': np.random.randint(0, 500, num_samples),  # Random hours since last maintenance
    'Failures': np.random.choice([0, 1], num_samples)  # Randomly assigning failures (0 = no failure, 1 = failure)
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to Excel
df.to_excel('synthetic_dataset.xlsx', index=False)

print("Synthetic dataset generated and saved as 'synthetic_dataset.xlsx'.")

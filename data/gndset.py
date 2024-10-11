import pandas as pd
import numpy as np

np.random.seed(42)
num_samples = 1000
machine_ids = np.random.randint(100, 500, size=num_samples)
temperature = np.random.normal(70, 10, size=num_samples)
pressure = np.random.normal(200, 15, size=num_samples)
vibration = np.random.normal(50, 5, size=num_samples)
power = np.random.normal(100, 20, size=num_samples)
hours_since_last_maintenance = np.random.normal(500, 100, size=num_samples)
failures = np.random.choice([0, 1], size=num_samples, p=[0.9, 0.1])

data = pd.DataFrame({
    'ID': machine_ids,
    'Temperature': temperature,
    'Pressure': pressure,
    'Vibration': vibration,
    'Power': power,
    'Hours_Since_Last_Maintenance': hours_since_last_maintenance,
    'Failures': failures
})

# Save the synthetic dataset
data.to_csv('data/raw/machine_data.csv', index=False)
print("Synthetic data generated and saved to 'data/raw/machine_data.csv'")

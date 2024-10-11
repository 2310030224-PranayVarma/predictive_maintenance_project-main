import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Function to load the raw data
def load_data(filepath):
    """
    Load the dataset from the given file path.
    Args:
        filepath (str): Path to the dataset (CSV file).
    Returns:
        pd.DataFrame: Loaded dataset as a pandas DataFrame or None if the file is not found.
    """
    if not os.path.exists(filepath):
        print(f"Error: File not found at {filepath}. Please check the file path.")
        return None
    
    try:
        data = pd.read_csv(filepath)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Function to clean the data
def clean_data(data):
    """
    Clean the dataset by handling missing values and removing unnecessary columns.
    Args:
        data (pd.DataFrame): Raw dataset.
    Returns:
        pd.DataFrame: Cleaned dataset.
    """
    if data is None:
        print("Error: Data is None. Exiting the process.")
        return None

    # Drop rows with missing values
    data = data.dropna()

    # Optionally remove unnecessary columns (like ID)
    if 'ID' in data.columns:
        data = data.drop('ID', axis=1)

    return data

# Function to scale the features
def scale_features(X_train, X_test):
    """
    Scale the features using StandardScaler.
    Args:
        X_train (pd.DataFrame): Training feature set.
        X_test (pd.DataFrame): Test feature set.
    Returns:
        np.array: Scaled X_train and X_test.
    """
    scaler = StandardScaler()

    # Fit scaler on the training data and apply it to both train and test sets
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled

# Function to preprocess the data
def preprocess_data(filepath):
    """
    Load, clean, and preprocess the data, and split into training and test sets.
    Args:
        filepath (str): Path to the dataset (CSV file).
    Returns:
        X_train, X_test, y_train, y_test: Processed and split features and labels.
    """
    # Load the raw data
    data = load_data(filepath)

    # Check if data loading was successful
    if data is None:
        print("Data loading failed. Exiting the process.")
        return None, None, None, None

    # Clean the data
    data = clean_data(data)

    # Ensure data cleaning was successful
    if data is None:
        print("Data cleaning failed. Exiting the process.")
        return None, None, None, None

    # Split features (X) and labels (y)
    X = data[['Temperature', 'Pressure', 'Vibration', 'Power', 'Hours_Since_Last_Maintenance']]
    y = data['Failures']

    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scale the features
    X_train_scaled, X_test_scaled = scale_features(X_train, X_test)

    # Save the processed data
    processed_data = pd.DataFrame(X_train_scaled, columns=['Temperature', 'Pressure', 'Vibration', 'Power', 'Hours_Since_Last_Maintenance'])
    processed_data['Failures'] = y_train.reset_index(drop=True)
    processed_data.to_csv('data/processed/processed_data.csv', index=False)

    return X_train_scaled, X_test_scaled, y_train, y_test

# Run the preprocessing
if __name__ == "__main__":
    filepath = 'data/raw/machine_data.csv'
    X_train, X_test, y_train, y_test = preprocess_data(filepath)
    if X_train is not None:
        print("Data preprocessing complete. Processed data saved to 'data/processed/processed_data.csv'.")

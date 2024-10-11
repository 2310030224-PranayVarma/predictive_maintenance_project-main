import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import pickle
from tkinter import ttk

# Function to load the trained model
def load_model(model_path):
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

# Function to make predictions on the uploaded file
def predict_failures(model, input_file):
    try:
        # Load the data from the Excel file
        data = pd.read_excel(input_file)

        # Preprocess the data (replace with actual preprocessing steps as per your model)
        features = data[['Temperature', 'Pressure', 'Vibration', 'Power', 'Hours_Since_Last_Maintenance']]

        # Make predictions
        predictions = model.predict(features)

        # Add predictions to the DataFrame
        data['Predicted Failures'] = predictions

        # Filter out rows where failure is predicted (assuming 1 indicates failure)
        failure_cases = data[data['Predicted Failures'] == 1]

        return data, failure_cases

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during prediction: {e}")
        return None, None

# Function to handle file selection
def select_file():
    
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if file_path:
        # Display the selected file path in the label
        file_label.config(text=f"Selected file: {file_path}")
        return file_path
    else:
        return None

# Function to show machines needing maintenance in a new window
def show_maintenance_window(failure_cases):
    maintenance_window = tk.Toplevel(app)
    maintenance_window.title("Machines Needing Maintenance")
    maintenance_window.geometry("500x400")

    # Create a frame for the maintenance data
    maintenance_frame = tk.Frame(maintenance_window)
    maintenance_frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Create a Treeview to display the maintenance cases
    columns = failure_cases.columns.tolist()  # Get the column names
    maintenance_tree = ttk.Treeview(maintenance_frame, columns=columns, show='headings')

    # Define column headings for maintenance Treeview
    for col in columns:
        maintenance_tree.heading(col, text=col)
        maintenance_tree.column(col, anchor="center")

    # Insert rows into the maintenance Treeview
    if failure_cases is not None and not failure_cases.empty:
        for index, row in failure_cases.iterrows():
            maintenance_tree.insert("", "end", values=list(row))

    # Create a scrollbar for the maintenance cases
    maintenance_scrollbar_y = ttk.Scrollbar(maintenance_frame, orient="vertical", command=maintenance_tree.yview)
    maintenance_tree.configure(yscrollcommand=maintenance_scrollbar_y.set)
    maintenance_scrollbar_y.pack(side="right", fill="y")

    maintenance_scrollbar_x = ttk.Scrollbar(maintenance_frame, orient="horizontal", command=maintenance_tree.xview)
    maintenance_tree.configure(xscrollcommand=maintenance_scrollbar_x.set)
    maintenance_scrollbar_x.pack(side="bottom", fill="x")

    # Pack the maintenance Treeview
    maintenance_tree.pack(side="left", fill="both", expand=True)

    # Count and display the number of machines needing maintenance
    count_label = tk.Label(maintenance_window, text=f"Total Machines Needing Maintenance: {len(failure_cases)}", font=("Arial", 12, "bold"))
    count_label.pack(pady=10)

# Function to run predictions and display the results
def run_predictions():
    input_file = select_file()
    if input_file:
        model = load_model('models/model.pkl')
        all_data, failure_cases = predict_failures(model, input_file)

        if all_data is not None:
            # Clear previous results in both frames
            for widget in loaded_frame.winfo_children():
                widget.destroy()
            for widget in maintenance_frame.winfo_children():
                widget.destroy()

            # Create a Treeview to display the loaded data
            columns = all_data.columns.tolist()  # Get the column names
            loaded_tree = ttk.Treeview(loaded_frame, columns=columns, show='headings')

            # Define column headings
            for col in columns:
                loaded_tree.heading(col, text=col)
                loaded_tree.column(col, anchor="center")

            # Insert rows into the loaded data Treeview
            for index, row in all_data.iterrows():
                loaded_tree.insert("", "end", values=list(row))

            # Create a scrollbar for the loaded data
            loaded_scrollbar_y = ttk.Scrollbar(loaded_frame, orient="vertical", command=loaded_tree.yview)
            loaded_tree.configure(yscrollcommand=loaded_scrollbar_y.set)
            loaded_scrollbar_y.pack(side="right", fill="y")

            loaded_scrollbar_x = ttk.Scrollbar(loaded_frame, orient="horizontal", command=loaded_tree.xview)
            loaded_tree.configure(xscrollcommand=loaded_scrollbar_x.set)
            loaded_scrollbar_x.pack(side="bottom", fill="x")

            # Pack the loaded data Treeview
            loaded_tree.pack(side="left", fill="both", expand=True)

            # Show maintenance window
            if failure_cases is not None and not failure_cases.empty:
                show_maintenance_window(failure_cases)

            # Create labels to indicate the sections
            loaded_label = tk.Label(app, text="Loaded Data:", font=("Arial", 12, "bold"))
            loaded_label.pack(pady=5)

        else:
            messagebox.showinfo("Info", "No data loaded.")

# Create the main application window
app = tk.Tk()
app.title("Predictive Maintenance - Failure Prediction")
app.geometry("1000x600")

# Create a label for instructions
instructions = tk.Label(app, text="Upload an Excel file to predict equipment failures:", font=("Arial", 14))
instructions.pack(pady=10)

# Create a button to select the file and run predictions
upload_button = tk.Button(app, text="Select File and Predict", command=run_predictions, font=("Arial", 12))
upload_button.pack(pady=10)

# Create a label to display the selected file path
file_label = tk.Label(app, text="No file selected", font=("Arial", 10), fg="gray")
file_label.pack(pady=5)

# Create frames for loaded data and maintenance cases
loaded_frame = tk.Frame(app)
loaded_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

maintenance_frame = tk.Frame(app)
maintenance_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

# Run the application
app.mainloop()

import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Gets the directory of utils.py
DATA_PATH = os.path.join(BASE_DIR, "../models/preprocessed_data.csv")

def load_data():
    try:
        df = pd.read_csv(DATA_PATH)
        print(f"Loaded dataset from: {DATA_PATH}")
        return df
    except FileNotFoundError:
        print(f"Dataset not found at: {DATA_PATH}")
        raise

def filter_doctors_by_time(df, user_time):
    # Filters doctors based on the given hour.
    return df[df["Hour"] == user_time]

def prepare_features(df_filtered):
    # Extracts relevant features for prediction.
    return df_filtered[["Hour", "Session Duration", "Count of Survey Attempts"]]

def save_predictions(df_filtered):
    # Ensure the 'outputs' directory exists
    output_dir = os.path.join(os.getcwd(), "outputs")  
    os.makedirs(output_dir, exist_ok=True)  # Create directory if it doesn't exist

    # Save the CSV file in the correct directory
    result_file = os.path.join(output_dir, "predicted_doctors.csv")
    df_filtered.to_csv(result_file, index=False)

    print(f"File saved at: {result_file}")
    return result_file

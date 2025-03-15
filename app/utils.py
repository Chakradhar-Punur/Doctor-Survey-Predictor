import pandas as pd
import os

def load_data(file_path="/Users/Chakradhar/doctor_survey_app/models/preprocessed_data.csv"):
    return pd.read_csv(file_path)

def filter_doctors_by_time(df, user_time):
    # Filters doctors based on the given hour.
    return df[df["Hour"] == user_time]

def prepare_features(df_filtered):
    # Extracts relevant features for prediction.
    return df_filtered[["Hour", "Session Duration", "Count of Survey Attempts"]]

def save_predictions(df_filtered):
    # Saves predictions to a CSV file and returns the filename.
    result_file = os.path.join("/Users/Chakradhar/doctor_survey_app/app/", "predicted_doctors.csv")
    df_filtered.to_csv(result_file, index=False)
    return result_file

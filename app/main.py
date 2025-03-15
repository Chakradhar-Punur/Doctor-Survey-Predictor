from flask import Flask, request, jsonify, render_template, send_file
import joblib
import os
from app.utils import load_data, filter_doctors_by_time, prepare_features, save_predictions

app = Flask(__name__, static_folder='../static', template_folder='../templates')

# Load the trained model
model = joblib.load("/Users/Chakradhar/doctor_survey_app/models/doctor_model.pkl")

df = load_data()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Predicts which doctors are likely to attend the survey at a given time.
    data = request.json
    user_time = int(data["time"])

    # Filter dataset
    df_filtered = filter_doctors_by_time(df, user_time)

    if df_filtered.empty:
        return jsonify({"message": "No doctors found for this time"})

    # Prepare features for model prediction
    X_new = prepare_features(df_filtered)
    df_filtered = df_filtered.copy()
    df_filtered["Prediction"] = model.predict(X_new)

    # Get only doctors likely to attend
    result_df = df_filtered[df_filtered["Prediction"] == 1][["NPI"]]

    if result_df.empty:
        return jsonify({"message": "No doctors predicted to attend at this time."})

    # Save and send CSV file
    result_file = save_predictions(result_df)
    
    # Verify file exists
    if not os.path.exists(result_file):
        return jsonify({"error": "Prediction file was not created."}), 500

    return send_file(result_file, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
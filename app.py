from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
import json
import os

# Load model, scaler, and label encoder
model = joblib.load("model.joblib")
scaler = joblib.load("scaler.joblib")
le = joblib.load("label_encoder.joblib")

app = Flask(__name__)

# Home page
@app.route("/")
def index():
    return render_template('index.html')

# All HTML pages routes
@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/signup")
def signup():
    return render_template('signup.html')

@app.route("/meditation_guides")
def meditation_guides():
    return render_template('meditation_guides.html')

@app.route("/relaxingmusic")
def relaxingmusic():
    return render_template('relaxingmusic.html')

@app.route("/stress_exercises")
def stress_exercises():
    return render_template('stress_exercises.html')

@app.route("/pattern")
def pattern():
    return render_template('pattern.html')

@app.route("/result")
def result():
    return render_template('result.html')

@app.route("/chatbot")
def chatbot():
    return render_template('chatbot.html')

# Stress prediction page
@app.route("/stress", methods=["GET", "POST"])
def home():
    prediction = None
    stress_level = None
    if request.method == "POST":
        try:
            form = request.form
            with open('model_features.json', 'r') as f:
                all_features = json.load(f)
            remove_cols = [
                "Do you attend classes regularly?",
                "Do you find that your relationship often causes you stress?",
                "Have you gained/lost weight?",
                "Have you noticed a rapid heartbeat or palpitations?",
                "Have you been getting headaches more often than usual?"
            ]
            model_features = [col for col in all_features if col not in remove_cols]
            input_data = {}
            missing_fields = []
            # Fill present features from form
            for col in model_features:
                val = form.get(col)
                if val is None or val == "":
                    missing_fields.append(col)
                else:
                    try:
                        input_data[col] = float(val)
                    except ValueError:
                        input_data[col] = 0
            input_data["Gender"] = form.get("Gender", "Male")
            # Fill removed features with default value (0)
            for col in remove_cols:
                input_data[col] = 0
            if missing_fields:
                prediction = f"Error: Missing fields: {', '.join(missing_fields)}"
            else:
                score = sum([input_data[col] for col in model_features if col != "Age"]) + float(input_data["Age"])
                # Ensure all features used in model are present in DataFrame
                df = pd.DataFrame([{k: input_data.get(k, 0) for k in all_features}])
                X = df[all_features].astype(float)
                X_scaled = scaler.transform(X)
                pred = model.predict(X_scaled)[0]
                stress_type = le.inverse_transform([pred])[0]
                prediction = f"Predicted Stress Type: {stress_type}"
                # Only show stress level for negative/distress types
                if "Eustress" in stress_type or "Positive" in stress_type:
                    stress_level = "Healthy/Positive Stress (No risk)"
                elif "No Stress" in stress_type:
                    stress_level = "Low"
                else:
                    if score <= 20:
                        stress_level = "Low"
                    elif score <= 40:
                        stress_level = "Medium"
                    elif score <= 60:
                        stress_level = "High"
                    else:
                        stress_level = "Ultra High"
        except Exception as e:
            prediction = f"Error: {str(e)}"
    return render_template('webpage.html', prediction=prediction, stress_level=stress_level)

# API endpoint for model training (from model.py)
@app.route("/train_model")
def train_model():
    try:
        # Import and run model training
        exec(open('model.py').read())
        return jsonify({"status": "success", "message": "Model trained successfully"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})
    
if __name__ == "__main__":
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

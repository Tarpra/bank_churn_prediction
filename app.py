from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd
import os

# Load model and scaler
model = joblib.load('random_forest_churn_model.pkl')
scaler = joblib.load('scaler.pkl')

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # ====== Read form inputs ======
        credit_score = float(request.form['CreditScore'])
        geography = request.form['Geography']
        gender = int(request.form['Gender'])
        age = float(request.form['Age'])
        tenure = int(request.form['Tenure'])
        balance = float(request.form['Balance'])
        num_of_products = int(request.form['NumOfProducts'])
        has_cr_card = int(request.form['HasCrCard'])
        is_active_member = int(request.form['IsActiveMember'])
        estimated_salary = float(request.form['EstimatedSalary'])

        # ====== One-hot encode Geography ======
        geo_germany = True if geography == 'Germany' else False
        geo_spain = True if geography == 'Spain' else False
        # France will be implied (both False)

        # ====== Create feature array ======
        features = np.array([[credit_score, gender, age, tenure, balance,
                              num_of_products, has_cr_card, is_active_member,
                              estimated_salary, geo_germany, geo_spain]])

        # ====== Scale and predict ======
        scaled_features = scaler.transform(features)
        prediction = model.predict(scaled_features)[0]
        probability = model.predict_proba(scaled_features)[0][1]

        # ====== Determine risk level ======
        if probability >= 0.7:
            risk_level = "High Risk"
        elif probability >= 0.4:
            risk_level = "Medium Risk"
        else:
            risk_level = "Low Risk"

        # ====== CSV File Path ======
        csv_path = r"C:\Users\Tarpr\Desktop\Bank_Churn_Prediction\Final Sem\bank_churn_dashboard_data.csv"

        # ====== Prepare new row ======
        new_data = {
            "CustomerId": "12345",
            "Surname": "12345",
            "CreditScore": credit_score,
            "Gender": gender,
            "Age": age,
            "Tenure": tenure,
            "EstimatedSalary": estimated_salary,
            "Balance": balance,
            "NumOfProducts": num_of_products,
            "HasCrCard": has_cr_card,
            "IsActiveMember": is_active_member,
            "Exited": int(prediction),
            "Geography_Germany": geo_germany,
            "Geography_Spain": geo_spain,
            "Churn_Probability": round(probability, 4),
            "Risk_Level": risk_level
        }

        # ====== Column Order (match existing CSV) ======
        columns_order = [
            "CustomerId", "Surname", "CreditScore", "Gender", "Age", "Tenure",
            "EstimatedSalary", "Balance", "NumOfProducts", "HasCrCard",
            "IsActiveMember", "Exited", "Geography_Germany", "Geography_Spain",
            "Churn_Probability", "Risk_Level"
        ]

        # ====== Append or create file ======
        if os.path.exists(csv_path):
            df = pd.read_csv(csv_path)
            new_row = pd.DataFrame([new_data])
            new_row = new_row[columns_order]
            df = pd.concat([df, new_row], ignore_index=True)
        else:
            df = pd.DataFrame([new_data], columns=columns_order)

        # ====== Fill Missing IDs/Surnames with 'Unknown' ======
        df['CustomerId'] = df['CustomerId'].fillna('Unknown')
        df['Surname'] = df['Surname'].fillna('Unknown')

        # ====== Save file (overwrite, no safe write) ======
        df.to_csv(csv_path, index=False)

        # ====== Return Web Output ======
        return f"""
        <h2>Churn Prediction Result</h2>
        <p><b>Prediction:</b> {'Churn' if prediction == 1 else 'Not Churn'}</p>
        <p><b>Churn Probability:</b> {round(probability * 100, 2)}%</p>
        <p><b>Risk Level:</b> {risk_level}</p>
        <a href="/">🔙 Try Again</a>
        """

    except Exception as e:
        return f"<p><b>Error:</b> {str(e)}</p>"

# ====== Run Flask App ======
if __name__ == '__main__':
    app.run(debug=True)

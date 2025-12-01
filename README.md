# bank_churn_prediction
End-to-end churn prediction project with ML modeling, data analysis, Flask deployment, and Power BI dashboarding.

# Bank Churn Prediction using Machine Learning & Flask Deployment

This project predicts customer churn for a bank using Machine Learning techniques and deploys the model using a simple Flask web application. It also includes a Power BI dashboard to visualize customer churn insights and explain business patterns behind churn.


##  Project Overview

Customer churn is a major challenge for banks. By identifying customers likely to leave, the bank can take preventive actions such as targeted offers, better services, and personalized communication.

This project includes:

- Machine Learning model predicting churn
- Data preprocessing & feature engineering
- Visual insights using Power BI
- Flask application for model deployment
- Jupyter Notebook demonstrating end-to-end analysis

##  Project Structure

Bank-Churn-Prediction/
│
├── dashboard/                     # Frontend/dashboard related files
│   ├── .gitkeep                   # Placeholder to keep the folder in Git
│   ├── Bank-Churn-Prediction-Using-Machine-Learning_Tarun.pptx  # PPT
│   └── BankChurn_ML_Model_Dashboard_Origibal.pbix # powerBi Dashboard
│
├── models/                        # Trained ML models and scalers
│   ├── placeholder.txt            # Placeholder file (can be removed)
│   ├── random_forest_churn_model.pkl  # Pickled Random Forest model
│   └── scaler.pkl                 # Pickled scaler object
│
├── app.py                         # Main Python script to run the app/dashboard
├── Bank Churn Project.ipynb        # Jupyter notebook with data analysis & model building
├── requirements.txt               # All project dependencies
├── README.md                       # Project documentation
├── LICENSE                         # License information
└── .gitignore                      # Files/folders to ignore in Git


---

## 🚀 Flask Deployment (Local)

To run the Flask application locally:

### 1. Create a virtual environment
python -m venv env


### 2. Activate the environment  
**Windows**

env\Scripts\activate

**Mac/Linux**
source env/bin/activate

### 3. Install dependencies

pip install -r requirements.txt


### 4. Run the application
python app.py


Flask will start at:
http://127.0.0.1:5000



---

## 📊 Power BI Dashboard

The project includes a Power BI dashboard with:

- Churn summary KPIs  
- Customer segmentation  
- Tenure, age, credit score analysis  
- Behavioral patterns behind churn  

To view the dashboard:

➡️ Download the `.pbix` file located in  
`dashboard/BankChurn_ML_Model_Dashboard_Original.pbix`  
➡️ Open it in **Power BI Desktop**

---

## 🧠 Machine Learning Workflow

The notebook covers:

1. **Exploratory Data Analysis (EDA)**
2. **Missing value handling**
3. **Feature encoding / scaling**
4. **Train/test split**
5. **Model training (Logistic Regression, Random Forest, XGBoost and tuning)**
6. **Evaluation metrics**
7. **Final model selection and saving**

---

## 📦 Model Deployment

The **app.py** file loads the trained ML model and exposes a simple web interface/API for predictions.

Users can input customer data and instantly get a prediction whether the customer is likely to churn.

---

## ✨ Key Skills Demonstrated

- Machine Learning  
- Flask deployment  
- Power BI dashboarding  
- Data preprocessing & feature engineering  
- Model evaluation  
- GitHub project structuring  
- Python (pandas, numpy, sklearn, flask)

---

## 📫 Contact

For any questions or collaborations, feel free to reach out @tanwartarun1810@gmail.com !




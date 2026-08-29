# 🌍 India AQI Prediction System

A Machine Learning based web application that predicts the **Air Quality Index (AQI)** and identifies the corresponding **AQI category** based on air pollutant concentrations, location, seasonal information, and historical PM2.5 data.

🔗 **Live Demo:** https://aqi-prediction-india-yash.streamlit.app/

---

## 🚀 Project Overview

Air pollution is a major environmental concern in India. This project uses Machine Learning techniques to predict AQI values based on multiple air pollutant measurements.

The application provides:

- AQI Prediction
- AQI Category Classification
- Air Pollutant Input Analysis
- City Selection
- Seasonal Information
- Historical PM2.5 Features
- Interactive Streamlit Web Interface

---

## 🧠 Machine Learning Models

This project uses two Machine Learning models:

### 1. AQI Regression Model

Predicts the numerical AQI value.

Example:

```text
Predicted AQI: 104.92
2. Classification Model

The classification model predicts the AQI category.

Example:

AQI Category: Satisfactory
📊 Input Features
Air Pollutants
PM2.5
PM10
NO
NO2
NOx
NH3
CO
SO2
O3
Benzene
Toluene
Location and Time
City
Year
Month
Season
Historical Information
Previous PM2.5 Value
3-Day Average PM2.5
🛠️ Tech Stack
Python
Pandas
NumPy
Scikit-learn
Joblib
Streamlit
Machine Learning
📂 Project Structure
AQI-Prediction-India/
│
├── data/
│   ├── processed/
│   └── raw/
│
├── models/
│   ├── aqi_classifier_model.pkl
│   ├── aqi_label_encoder.pkl
│   ├── aqi_regression_model.pkl
│   ├── classification_features.pkl
│   └── regression_features.pkl
│
├── notebooks/
│
├── reports/
│
├── src/
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
⚙️ Installation
1. Clone the Repository
git clone https://github.com/guptayash122006/AQI-Prediction-India.git
2. Navigate to the Project Folder
cd AQI-Prediction-India
3. Create a Virtual Environment
python -m venv venv
4. Activate the Virtual Environment
Windows
venv\Scripts\activate
5. Install Dependencies
pip install -r requirements.txt
▶️ Run the Application

Run the following command:

streamlit run main.py

The application will start locally at:

http://localhost:8501
🔄 Project Workflow
AQI Dataset
     ↓
Data Understanding
     ↓
Data Cleaning & Preprocessing
     ↓
Feature Engineering
     ↓
Model Training
     ↓
Regression Model
     +
Classification Model
     ↓
Model Serialization
     ↓
Streamlit Web Application
     ↓
AQI Prediction
📈 Example Prediction
Output	Example Result
Predicted AQI	104.92
AQI Category	Satisfactory
🔮 Future Improvements
Real-time Air Quality API Integration
Interactive Data Visualizations
AQI Trend Analysis
Model Performance Dashboard
More Indian Cities
Docker Deployment
Cloud-based Model Deployment
👨‍💻 Author

Yash Gupta

Aspiring Data Scientist | Machine Learning Enthusiast

🔗 GitHub: https://github.com/guptayash122006


### Ab kya karna hai

1. VS Code me `README.md` open karo.
2. **Ctrl + A → Delete**
3. Upar wala pura code paste karo.
4. `YOUR_STREAMLIT_APP_LINK` ki jagah apna Streamlit URL paste karo.
5. Save: **Ctrl + S**
6. Terminal me:

```bash
git add README.md
git commit -m "Update project README"
git push origin main

Important: Is README me fake accuracy, fake dataset size, ya fake model performance maine intentionally nahi likha. Agar tumhare actual notebook se model accuracy/R²/MAE nikal lete hain, tab ek proper Model Performance section bhi add karenge. Ye LinkedIn aur recruiters ke liye project ko aur credible banayega.

# 🌍 India AQI Prediction System

An end-to-end Machine Learning application that predicts the **Air Quality Index (AQI)** and its corresponding **AQI Category** using air pollutant data, location, time, and historical PM2.5 information.

## 🚀 Live Demo

🔗 **Streamlit App:** https://aqi-prediction-india-yash.streamlit.app/

🔗 **GitHub Repository:** https://github.com/guptayash122006/AQI-Prediction-India

---

## 📌 Project Overview

Air pollution is a major environmental concern in India. This project applies Machine Learning techniques to analyze air pollutant data and predict:

- Numerical AQI Value
- AQI Category

The application provides an interactive Streamlit interface where users can enter pollutant values and environmental information to receive predictions.

---

## ✨ Features

- 🌫️ AQI Value Prediction
- 📊 AQI Category Classification
- 🏙️ Indian City Selection
- 🌦️ Seasonal Information
- 📈 Historical PM2.5 Features
- 🧠 Machine Learning Models
- 🖥️ Interactive Streamlit Web Application
- ☁️ Cloud Deployment

---

## 🧠 Machine Learning Models

This project uses two Machine Learning models.

### 1. AQI Regression Model

The regression model predicts the numerical AQI value.

Example:

```text
Predicted AQI: 104.92
```

### 2. AQI Classification Model

The classification model predicts the AQI category.

Example:

```text
AQI Category: Satisfactory
```

---

## 📊 Input Features

### Air Pollutants

- PM2.5
- PM10
- NO
- NO2
- NOx
- NH3
- CO
- SO2
- O3
- Benzene
- Toluene

### Location and Time

- City
- Year
- Month
- Season

### Historical Information

- Previous PM2.5 Value
- 3-Day Average PM2.5

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Machine Learning

---

## 📂 Project Structure

```text
AQI-Prediction-India/
│
├── data/
│   ├── raw/
│   └── processed/
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
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/guptayash122006/AQI-Prediction-India.git
```

### 2. Navigate to the Project Directory

```bash
cd AQI-Prediction-India
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Run:

```bash
streamlit run main.py
```

The application will start locally at:

```text
http://localhost:8501
```

---

## 🔄 Project Workflow

```text
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
Regression Model + Classification Model
     ↓
Model Serialization
     ↓
Streamlit Web Application
     ↓
AQI Prediction
```

---

## 📈 Example Output

| Output | Example Result |
|---|---|
| Predicted AQI | 104.92 |
| AQI Category | Satisfactory |

---

## 🔮 Future Improvements

- Real-time Air Quality API integration
- Interactive data visualizations
- AQI trend analysis
- Model performance dashboard
- Support for more Indian cities
- Docker containerization

---

## 👨‍💻 Author

**Yash Gupta**

Aspiring Data Scientist | Machine Learning Enthusiast

🔗 GitHub: https://github.com/guptayash122006

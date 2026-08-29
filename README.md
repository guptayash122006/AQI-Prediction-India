# 🌍 India AQI Prediction System

An end-to-end Machine Learning application that predicts the **Air Quality Index (AQI)** and its corresponding **AQI Category** using air pollutant concentrations, location, time, and historical PM2.5 information.

---

## 🚀 Live Demo

🔗 **Streamlit App:** https://aqi-prediction-india-yash.streamlit.app/

🔗 **GitHub Repository:** https://github.com/guptayash122006/AQI-Prediction-India

---

## 📌 Project Overview

Air pollution is a major environmental concern in India. This project applies Machine Learning techniques to analyze air pollutant data and predict both the numerical AQI value and its corresponding AQI category.

The application provides an interactive Streamlit interface where users can enter pollutant concentrations, location information, seasonal data, and historical PM2.5 values to generate predictions.

---

## ✨ Features

- 🌫️ AQI Value Prediction
- 📊 AQI Category Classification
- 🏙️ Indian City Selection
- 🌦️ Seasonal Information
- 📈 Historical PM2.5 Features
- 🧠 Machine Learning-Based Predictions
- 🖥️ Interactive Streamlit Web Application
- ☁️ Cloud Deployment

---

## 🖥️ Application Preview

### Home Page

![India AQI Prediction System - Home](images/home_page.png)

### AQI Prediction Input Interface

![AQI Prediction Input Interface](images/prediction_input.png)

---

## 🧠 Machine Learning Models

This project uses two Machine Learning models to generate predictions.

### 1. AQI Regression Model

The regression model predicts the numerical Air Quality Index value.

**Example:**

```text
Predicted AQI: 104.92
```

### 2. AQI Classification Model

The classification model predicts the AQI category based on the provided environmental and pollutant data.

**Example:**

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

### Location and Time Information

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
├── images/
│   ├── app-preview.png
│   └── project-structure.png
|
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

### Project Structure Visualization

![Project Structure](images/project-structure.png)

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

Run the following command:

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

## 📈 Example Prediction

| Output | Example Result |
|---|---|
| Predicted AQI | 104.92 |
| AQI Category | Satisfactory |

---

## 🔮 Future Improvements

- Real-time Air Quality API Integration
- Interactive Data Visualizations
- AQI Trend Analysis
- Model Performance Dashboard
- Support for More Indian Cities
- Docker Containerization
- Cloud-Based Deployment Improvements

---

## 👨‍💻 Author

**Yash Gupta**

Aspiring Data Scientist | Machine Learning Enthusiast

🔗 GitHub: https://github.com/guptayash122006

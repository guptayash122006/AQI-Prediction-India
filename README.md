AQI-Prediction-India/
│
├── app/
│   └── app.py                 # Streamlit app (Day 7)
│
├── data/
│   ├── raw/
│   │   └── city_day.csv       # Original dataset
│   │
│   └── processed/             # Cleaned dataset
│
├── models/                    # Saved ML models (.pkl/.joblib)
│
├── notebooks/
│   └── Day1_Data_Understanding.ipynb
│
├── reports/
│   ├── images/                # Graphs and plots
│   └── progress.md            # Daily progress
│
├── src/
│   ├── __init__.py
│   ├── config.py              # Project constants/paths
│   ├── data_loader.py         # Load dataset
│   ├── preprocessing.py       # Cleaning & preprocessing
│   ├── feature_engineering.py # Feature creation
│   ├── train_regression.py    # AQI prediction model
│   ├── train_classifier.py    # Health risk classification
│   ├── evaluate.py            # Model evaluation
│   └── utils.py               # Helper functions
│
├── .gitignore
├── README.md
├── requirements.txt
└── main.py                    # Main entry point (optional)
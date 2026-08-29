import streamlit as st
import joblib
import pandas as pd
from pathlib import Path


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="India AQI Prediction System",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.main-title {
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 18px;
    color: #A0A6B0;
    margin-bottom: 30px;
}

.section-title {
    font-size: 27px;
    font-weight: 600;
    margin-top: 25px;
    margin-bottom: 15px;
}

.result-card {
    background-color: #1E2530;
    padding: 25px;
    border-radius: 12px;
    text-align: center;
}

.footer {
    text-align: center;
    color: #808080;
    margin-top: 50px;
    padding-top: 20px;
}

</style>
""", unsafe_allow_html=True)


# ==================================================
# LOAD MODELS
# ==================================================

BASE_DIR = Path(__file__).resolve().parent
MODELS_DIR = BASE_DIR / "models"


@st.cache_resource
def load_models():

    regression_model = joblib.load(
        MODELS_DIR / "aqi_regression_model.pkl"
    )

    classifier_model = joblib.load(
        MODELS_DIR / "aqi_classifier_model.pkl"
    )

    label_encoder = joblib.load(
        MODELS_DIR / "aqi_label_encoder.pkl"
    )

    regression_features = joblib.load(
        MODELS_DIR / "regression_features.pkl"
    )

    classification_features = joblib.load(
        MODELS_DIR / "classification_features.pkl"
    )

    return (
        regression_model,
        classifier_model,
        label_encoder,
        regression_features,
        classification_features
    )


try:

    (
        regression_model,
        classifier_model,
        label_encoder,
        regression_features,
        classification_features
    ) = load_models()

except FileNotFoundError as e:

    st.error("❌ Model files not found!")

    st.write(
        "Make sure these files exist inside the models folder:"
    )

    st.code("""
models/
│
├── aqi_regression_model.pkl
├── aqi_classifier_model.pkl
├── aqi_label_encoder.pkl
├── regression_features.pkl
└── classification_features.pkl
    """)

    st.stop()


# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.title("🌍 AQI Prediction")

st.sidebar.markdown("---")

st.sidebar.info("""
### How to use

1. Enter pollutant values.
2. Select city.
3. Select season.
4. Enter PM2.5 historical values.
5. Click **Predict AQI**.
""")

st.sidebar.markdown("---")

st.sidebar.write(
    "Machine Learning Project"
)

st.sidebar.caption(
    "Regression + Classification Models"
)


# ==================================================
# TITLE
# ==================================================

st.markdown(
    '<div class="main-title">🌍 India AQI Prediction System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Predict Air Quality Index (AQI) and AQI Category using Machine Learning.'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# ==================================================
# AIR POLLUTANT INPUT
# ==================================================

st.markdown(
    '<div class="section-title">Enter Air Pollutant Values</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)


# ---------------- COLUMN 1 ----------------

with col1:

    pm25 = st.number_input(
        "PM2.5",
        min_value=0.0,
        value=50.0
    )

    pm10 = st.number_input(
        "PM10",
        min_value=0.0,
        value=80.0
    )

    no = st.number_input(
        "NO",
        min_value=0.0,
        value=10.0
    )

    no2 = st.number_input(
        "NO2",
        min_value=0.0,
        value=20.0
    )

    nox = st.number_input(
        "NOx",
        min_value=0.0,
        value=30.0
    )


# ---------------- COLUMN 2 ----------------

with col2:

    nh3 = st.number_input(
        "NH3",
        min_value=0.0,
        value=10.0
    )

    co = st.number_input(
        "CO",
        min_value=0.0,
        value=1.0
    )

    so2 = st.number_input(
        "SO2",
        min_value=0.0,
        value=10.0
    )

    o3 = st.number_input(
        "O3",
        min_value=0.0,
        value=30.0
    )

    benzene = st.number_input(
        "Benzene",
        min_value=0.0,
        value=1.0
    )


# ---------------- COLUMN 3 ----------------

with col3:

    toluene = st.number_input(
        "Toluene",
        min_value=0.0,
        value=1.0
    )

    year = st.number_input(
        "Year",
        min_value=2015,
        max_value=2035,
        value=2026
    )

    month = st.selectbox(
        "Month",
        list(range(1, 13))
    )


# ==================================================
# LOCATION AND TIME
# ==================================================

st.markdown(
    '<div class="section-title">Location and Time Information</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)


cities = [
    "Ahmedabad",
    "Amaravati",
    "Amritsar",
    "Bengaluru",
    "Bhopal",
    "Brajrajnagar",
    "Chandigarh",
    "Chennai",
    "Coimbatore",
    "Delhi",
    "Gurugram",
    "Guwahati",
    "Hyderabad",
    "Jaipur",
    "Jorapokhar",
    "Kolkata",
    "Lucknow",
    "Mumbai",
    "Patna",
    "Shillong",
    "Talcher",
    "Thiruvananthapuram",
    "Visakhapatnam"
]


with col1:

    city = st.selectbox(
        "Select City",
        cities
    )


with col2:

    season = st.selectbox(
        "Select Season",
        [
            "Winter",
            "Summer",
            "Monsoon",
            "Post-Monsoon"
        ]
    )


# ==================================================
# HISTORICAL INFORMATION
# ==================================================

st.markdown(
    '<div class="section-title">PM2.5 Historical Information</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)


with col1:

    pm25_lag1 = st.number_input(
        "Previous PM2.5 Value",
        min_value=0.0,
        value=50.0
    )


with col2:

    pm25_rolling3 = st.number_input(
        "3-Day Average PM2.5",
        min_value=0.0,
        value=50.0
    )


st.write("")


# ==================================================
# PREDICT BUTTON
# ==================================================

predict_button = st.button(
    "🔮 Predict AQI",
    use_container_width=True
)


# ==================================================
# AQI CATEGORY DESCRIPTION
# ==================================================

def get_aqi_message(category):

    messages = {

        "Good":
        "Air quality is considered satisfactory and poses little or no risk.",

        "Satisfactory":
        "Air quality is acceptable, but sensitive individuals may experience minor discomfort.",

        "Moderately Polluted":
        "People with respiratory conditions may experience discomfort.",

        "Poor":
        "Prolonged exposure may cause breathing discomfort for many people.",

        "Very Poor":
        "Health effects may become more serious, especially for sensitive groups.",

        "Severe":
        "Air quality is hazardous and may seriously affect health."
    }

    return messages.get(
        category,
        "AQI category predicted successfully."
    )


# ==================================================
# MAKE PREDICTION
# ==================================================

if predict_button:

    # ----------------------------------------------
    # RAW INPUT DATA
    # ----------------------------------------------

    input_data = {

        "PM2.5": pm25,
        "PM10": pm10,
        "NO": no,
        "NO2": no2,
        "NOx": nox,
        "NH3": nh3,
        "CO": co,
        "SO2": so2,
        "O3": o3,
        "Benzene": benzene,
        "Toluene": toluene,
        "Year": year,
        "Month": month,
        "PM2.5_lag1": pm25_lag1,
        "PM2.5_rolling3": pm25_rolling3
    }


    # ----------------------------------------------
    # CREATE DATAFRAME
    # ----------------------------------------------

    input_df = pd.DataFrame(
        [input_data]
    )


    # ----------------------------------------------
    # ADD ALL REGRESSION FEATURES
    # ----------------------------------------------

    for feature in regression_features:

        if feature not in input_df.columns:

            input_df[feature] = 0


    # ----------------------------------------------
    # CITY ONE-HOT ENCODING
    # ----------------------------------------------

    city_column = f"City_{city}"

    if city_column in input_df.columns:

        input_df[city_column] = 1


    # ----------------------------------------------
    # SEASON ONE-HOT ENCODING
    # ----------------------------------------------

    season_column = f"Season_{season}"

    if season_column in input_df.columns:

        input_df[season_column] = 1


    # ----------------------------------------------
    # REGRESSION INPUT
    # ----------------------------------------------

    regression_input = input_df.reindex(
        columns=regression_features,
        fill_value=0
    )


    # ----------------------------------------------
    # AQI PREDICTION
    # ----------------------------------------------

    predicted_aqi = regression_model.predict(
        regression_input
    )[0]


    # Prevent negative AQI prediction

    predicted_aqi = max(
        0,
        predicted_aqi
    )


    # ----------------------------------------------
    # CLASSIFICATION INPUT
    # ----------------------------------------------

    classification_input = input_df.reindex(
        columns=classification_features,
        fill_value=0
    )


    # ----------------------------------------------
    # AQI CATEGORY PREDICTION
    # ----------------------------------------------

    predicted_class = classifier_model.predict(
        classification_input
    )

    predicted_bucket = label_encoder.inverse_transform(
        predicted_class
    )[0]


    # ==================================================
    # RESULTS
    # ==================================================

    st.divider()

    st.markdown(
        '<div class="section-title">Prediction Results</div>',
        unsafe_allow_html=True
    )

    result_col1, result_col2 = st.columns(2)


    # AQI RESULT

    with result_col1:

        st.metric(
            label="Predicted AQI",
            value=f"{predicted_aqi:.2f}"
        )


    # CATEGORY RESULT

    with result_col2:

        st.metric(
            label="Predicted AQI Category",
            value=predicted_bucket
        )


    # ----------------------------------------------
    # AQI MESSAGE
    # ----------------------------------------------

    message = get_aqi_message(
        predicted_bucket
    )

    st.info(
        f"ℹ️ {message}"
    )


    # ----------------------------------------------
    # SUCCESS
    # ----------------------------------------------

    st.success(
        "✅ Prediction completed successfully!"
    )


# ==================================================
# FOOTER
# ==================================================

st.markdown(
    """
    <div class="footer">
        🌍 <b>AQI Prediction India</b> | Machine Learning Project
    </div>
    """,
    unsafe_allow_html=True
)
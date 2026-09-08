
import streamlit as st
import pickle
import numpy as np
import time

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Student Result Predictor",
    page_icon="🎓",
    layout="centered"
)

# -------------------------------------------------
# CUSTOM CSS
# -------------------------------------------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #0f172a, #1e3a5f);
}

.main-title {
    text-align: center;
    color: white;
    font-size: 42px;
    font-weight: bold;
    margin-bottom: 0px;
}

.subtitle {
    text-align: center;
    color: #cbd5e1;
    font-size: 17px;
    margin-bottom: 30px;
}

div.stButton > button {
    width: 100%;
    height: 55px;
    border-radius: 12px;
    border: none;
    background: linear-gradient(90deg, #2563eb, #06b6d4);
    color: white;
    font-size: 20px;
    font-weight: bold;
    transition: 0.3s;
}

div.stButton > button:hover {
    transform: scale(1.03);
    box-shadow: 0px 0px 20px #06b6d4;
}

.result-box {
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    font-size: 25px;
    font-weight: bold;
    background: linear-gradient(135deg, #16a34a, #22c55e);
    color: white;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)


# -------------------------------------------------
# LOAD MODEL
# -------------------------------------------------
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as file:
        model = pickle.load(file)
    return model


try:
    model = load_model()
except FileNotFoundError:
    st.error("❌ model.pkl file not found. Please upload it to the same folder.")
    st.stop()


# -------------------------------------------------
# HEADER
# -------------------------------------------------
st.markdown(
    '<p class="main-title">🎓 Student Result Predictor</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">Enter student marks and predict the result using Machine Learning 🤖</p>',
    unsafe_allow_html=True
)


# -------------------------------------------------
# INPUTS
# -------------------------------------------------
st.subheader("📝 Enter Subject Marks")

col1, col2 = st.columns(2)

with col1:
    hindi = st.number_input("📘 Hindi", 0, 100, 50)
    science = st.number_input("🔬 Science", 0, 100, 50)
    history = st.number_input("📜 History", 0, 100, 50)

with col2:
    english = st.number_input("📕 English", 0, 100, 50)
    maths = st.number_input("📐 Maths", 0, 100, 50)
    geography = st.number_input("🌍 Geography", 0, 100, 50)


# -------------------------------------------------
# CALCULATE TOTAL
# -------------------------------------------------
total = hindi + english + science + maths + history + geography

st.info(f"📊 Total Marks: {total} / 600")


# -------------------------------------------------
# PREDICTION
# -------------------------------------------------
if st.button("🚀 Predict Result"):

    with st.spinner("🤖 AI is analyzing student performance..."):

        progress = st.progress(0)

        for i in range(100):
            time.sleep(0.01)
            progress.progress(i + 1)

    # Input data in exact training order
    input_data = np.array([
        [
            hindi,
            english,
            science,
            maths,
            history,
            geography,
            total
        ]
    ])

    try:
        prediction = model.predict(input_data)

        st.balloons()

        st.markdown(
            f"""
            <div class="result-box">
                🎯 Prediction Complete! <br><br>
                Student Result: {prediction[0]}
            </div>
            """,
            unsafe_allow_html=True
        )

    except Exception as e:
        st.error(f"Prediction Error: {e}")


# -------------------------------------------------
# FOOTER
# -------------------------------------------------
st.markdown("---")

st.markdown(
    "<center>🤖 Built with Machine Learning & Streamlit</center>",
    unsafe_allow_html=True
)


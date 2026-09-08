
import pickle
import numpy as np
import time

st.set_page_config(
    page_title="Student Result Predictor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>

    /* Main Background */
    .stApp {
        background: linear-gradient(135deg, #141E30, #243B55);
        color: white;
    }

    /* Title */
    .main-title {
        text-align: center;
        font-size: 45px;
        font-weight: bold;
        color: #ffffff;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #cbd5e1;
        margin-bottom: 30px;
    }

    /* Card */
    .card {
        background: rgba(255,255,255,0.08);
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0px 8px 25px rgba(0,0,0,0.3);
        backdrop-filter: blur(10px);
        margin-bottom: 20px;
    }

    /* Predict Button */
    div.stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #00c6ff, #0072ff);
        color: white;
        border-radius: 12px;
        height: 55px;
        font-size: 20px;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }

    div.stButton > button:hover {
        transform: scale(1.03);
        box-shadow: 0px 0px 20px #00c6ff;
    }

    /* Result Box */
    .result-card {
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        margin-top: 25px;
        background: linear-gradient(135deg, #11998e, #38ef7d);
        color: white;
        animation: fadeIn 1s;
    }

    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0px);
        }
    }

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as file:
        model = pickle.load(file)
    return model


model = load_model()


# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.markdown(
    '<div class="main-title">🎓 Student Result Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Enter subject marks and predict the student result using Machine Learning 🤖</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# INPUT SECTION
# --------------------------------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("📝 Enter Student Marks")

col1, col2 = st.columns(2)

with col1:
    hindi = st.number_input(
        "📘 Hindi Marks",
        min_value=0.0,
        max_value=100.0,
        value=50.0
    )

    science = st.number_input(
        "🔬 Science Marks",
        min_value=0.0,
        max_value=100.0,
        value=50.0
    )

    history = st.number_input(
        "📜 History Marks",
        min_value=0.0,
        max_value=100.0,
        value=50.0
    )


with col2:
    english = st.number_input(
        "📕 English Marks",
        min_value=0.0,
        max_value=100.0,
        value=50.0
    )

    maths = st.number_input(
        "📐 Maths Marks",
        min_value=0.0,
        max_value=100.0,
        value=50.0
    )

    geography = st.number_input(
        "🌍 Geography Marks",
        min_value=0.0,
        max_value=100.0,
        value=50.0
    )


# Automatically Calculate Total
total = hindi + english + science + maths + history + geography

st.info(f"📊 **Calculated Total Marks: {total:.0f}**")

st.markdown('</div>', unsafe_allow_html=True)


# --------------------------------------------------
# PREDICT BUTTON
# --------------------------------------------------
if st.button("🚀 Predict Result"):

    # Loading Effect
    with st.spinner("🤖 AI is analyzing student performance..."):

        progress_bar = st.progress(0)

        for percent_complete in range(100):
            time.sleep(0.01)
            progress_bar.progress(percent_complete + 1)

    # Input Array
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

    # Prediction
    prediction = model.predict(input_data)

    # Result
    st.balloons()

    st.markdown(
        f"""
        <div class="result-card">
            🎯 Prediction Complete! <br><br>
            Student Result: <b>{prediction[0]}</b>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")

st.markdown(
    """
    <center>
    🤖 Machine Learning Powered Student Result Prediction System <br>
    Built with ❤️ using Streamlit & Scikit-learn
    </center>
    """,
    unsafe_allow_html=True
)
```

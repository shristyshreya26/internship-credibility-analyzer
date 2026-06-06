import streamlit as st
import joblib

from scipy.sparse import hstack

from utils import (
    clean_text,
    extract_features
)

st.markdown("""
<h1 style='text-align:center;'>
🔍 Internship Credibility Analyzer
</h1>
<p style='text-align:center; font-size:18px;'>
AI-powered internship scam detection and credibility assessment
</p>
""", unsafe_allow_html=True)

st.write(
    "Analyze internship postings and estimate credibility."
)

from pathlib import Path
import joblib

BASE_DIR = Path(__file__).resolve().parent.parent

model = joblib.load(
    BASE_DIR / "models" / "fraud_detector.pkl"
)

vectorizer = joblib.load(
    BASE_DIR / "models" / "tfidf_vectorizer.pkl"
)

user_text = st.text_area(
    "📄 Paste Internship Posting",
    height=250,
    placeholder="""
Example:
Software Development Intern
Duration: 6 months
Stipend: ₹20,000/month
Apply through company website...
    """
)

if st.button("Analyze Internship",
    "use_container_width=True"):
    cleaned = clean_text(user_text)
    text_features = vectorizer.transform([cleaned])
    extra_features = extract_features(user_text)
   
    final_features = hstack(
    [text_features,
     [extra_features]]
    )
    
    probs = model.predict_proba(
        final_features
    )[0]
    
   

    fraud_prob = probs[0]

    legit_prob = probs[1]

    credibility_score = int(
        legit_prob * 100
    )
    if credibility_score >= 80:
        label = "Likely Legitimate"

    elif credibility_score >= 50:
        label = "Needs Verification"

    else:
        label = "Likely Suspicious"

    if credibility_score >= 85:
        color = "#28a745"
    elif credibility_score >= 50:
        color = "#ffc107"
    else:
        color = "#dc3545"
        
    st.metric(
    "Fraud Probability",
    f"{fraud_prob*100:.1f}%"
    )
    st.metric(
    "Legitimacy Probability",
    f"{legit_prob*100:.1f}%"
    )
    st.subheader("⚠ Detected Risk Factors")
    if extra_features[0]:
        st.warning("WhatsApp-based application detected")

    if extra_features[1]:
        st.warning("Registration fee requested")

    if extra_features[4]:
        st.warning("No interview mentioned")

    if extra_features[5]:
        st.warning("Daily earning claim detected")

    st.subheader("Confidence")

    st.progress(
    credibility_score/100
    )


    st.markdown(f"""
    <div style="
    padding:20px;
    border-radius:15px;
    background-color:{color};
    color:white;
    text-align:center;
    font-size:32px;
    font-weight:bold;">
    Credibility Score: {credibility_score}/100
    </div>
    """, unsafe_allow_html=True)

    st.write(
        f"Assessment: {label}"
    )

    reasons = []
    if extra_features[0]:
        reasons.append("WhatsApp application detected")

    if extra_features[1]:
        reasons.append("Registration fee requested")

    if extra_features[6] < 150:
        reasons.append("Very short posting")


with st.sidebar:

    st.header("Sample Inputs")

    st.info("""
    Legitimate Example:
    
    Software Development Intern
    Duration: 6 months
    Stipend: ₹20,000/month
    """)

    st.warning("""
    Suspicious Example:
    
    Earn ₹5000 daily
    No interview
    WhatsApp now
    """)

st.markdown("---")

st.caption(
    "Developed using Machine Learning, TF-IDF and Logistic Regression"
)









import datetime
import streamlit as st
from agents.stress_predictor import display_travel_stress_predictor

# Configure the page
st.set_page_config(
    page_title="AI Travel Stress Predictor",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Perfect Professional UI Styles - MVP Ready + DROPDOWN FIXES
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        .stApp {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            font-family: 'Inter', sans-serif;
        }
        
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #ffffff 0%, #f8f9fa 100%);
            border-right: 3px solid #e9ecef;
        }
        
        section[data-testid="stSidebar"] .stRadio > div {
            color: #2c3e50 !important;
            font-weight: 600 !important;
            font-size: 16px !important;
        }
        
        section[data-testid="stSidebar"] h1, 
        section[data-testid="stSidebar"] h2, 
        section[data-testid="stSidebar"] h3 {
            color: #2c3e50 !important;
            font-weight: 700 !important;
        }
        
        .main-content {
            background: white !important;
            border-radius: 20px !important;
            padding: 30px !important;
            margin: 20px !important;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1) !important;
            border: 1px solid #e9ecef !important;
        }
        
        h1, h2, h3, h4, h5, h6, p, span, div, label {
            color: #2c3e50 !important;
        }
        
        h1 {
            font-weight: 700 !important;
            text-align: center !important;
            margin-bottom: 10px !important;
            font-size: 2.5rem !important;
        }
        
        h2, h3, h4 {
            font-weight: 600 !important;
            margin-top: 25px !important;
        }
        
        /* CRITICAL DROPDOWN FIXES */
        .stTextInput > div > div > input,
        .stSelectbox > div > div > div,
        .stSlider > div > div > div {
            background-color: #ffffff !important;
            color: #2c3e50 !important;
            border: 2px solid #e9ecef !important;
            border-radius: 8px !important;
            font-weight: 500 !important;
        }
        
        .stSelectbox > div > div > div {
            background-color: white !important;
            color: #2c3e50 !important;
        }
        
        .stSelectbox > div > div > div > div {
            background-color: white !important;
            color: #2c3e50 !important;
        }
        
        div[data-baseweb="select"] > div {
            background-color: white !important;
            color: #2c3e50 !important;
        }
        
        div[data-baseweb="select"] * {
            color: #2c3e50 !important;
            background-color: white !important;
        }
        
        .stTextInput > div > div > input:focus,
        .stSelectbox > div > div > div:focus {
            border-color: #3498db !important;
            box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.1) !important;
        }
        
        label, .stSlider label, .stSelectbox label, .stTextInput label {
            color: #2c3e50 !important;
            font-size: 16px !important;
            font-weight: 600 !important;
        }
        
        .stButton > button {
            background: linear-gradient(135deg, #3498db 0%, #2980b9 100%) !important;
            color: white !important;
            border: none !important;
            border-radius: 10px !important;
            font-weight: 600 !important;
            padding: 12px 24px !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 4px 15px rgba(52, 152, 219, 0.3) !important;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 6px 20px rgba(52, 152, 219, 0.4) !important;
        }
        
        button[kind="primary"] {
            background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%) !important;
            font-size: 18px !important;
            padding: 15px 30px !important;
        }
        
        .stAlert {
            border-radius: 10px !important;
            border: none !important;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1) !important;
        }
        
        .stSuccess {
            background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%) !important;
            color: #155724 !important;
        }
        
        .stInfo {
            background: linear-gradient(135deg, #d1ecf1 0%, #bee5eb 100%) !important;
            color: #0c5460 !important;
        }
        
        .stWarning {
            background: linear-gradient(135deg, #fff3cd 0%, #ffeaa7 100%) !important;
            color: #856404 !important;
        }
        
        .stError {
            background: linear-gradient(135deg, #f8d7da 0%, #f5c6cb 100%) !important;
            color: #721c24 !important;
        }
        
        .mvp-badge {
            background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%) !important;
            color: white !important;
            padding: 8px 16px !important;
            border-radius: 20px !important;
            font-size: 14px !important;
            font-weight: 600 !important;
            margin: 10px 0 !important;
            display: inline-block !important;
        }
        
        .stProgress > div > div > div {
            background: linear-gradient(135deg, #3498db 0%, #2980b9 100%) !important;
        }
        
        .stCheckbox > label {
            color: #2c3e50 !important;
            font-weight: 500 !important;
        }
        
        .stRadio > div > label {
            color: #2c3e50 !important;
            font-weight: 500 !important;
        }
        
        .streamlit-expanderHeader {
            background: white !important;
            color: #2c3e50 !important;
        }
        
        .block-container {
            padding-top: 1rem !important;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation with BABY FEET ICON
st.sidebar.markdown("## 👶 AI Travel Stress Predictor")
st.sidebar.markdown('<div class="mvp-badge">🚧 Beta Version</div>', unsafe_allow_html=True)

# FEEDBACK POPUP IMPLEMENTATION
if st.sidebar.button("💬 Give Feedback", use_container_width=True):
    with st.sidebar.form("feedback_form"):
        st.markdown("### 📝 Help Us Improve!")
        
        rating = st.selectbox("How would you rate the app?", [
            "⭐⭐⭐⭐⭐ Excellent (5/5)",
            "⭐⭐⭐⭐ Good (4/5)", 
            "⭐⭐⭐ Average (3/5)",
            "⭐⭐ Poor (2/5)",
            "⭐ Very Poor (1/5)"
        ])
        
        feedback_type = st.selectbox("What kind of feedback?", [
            "🐛 Bug Report",
            "💡 Feature Request", 
            "🎨 UI/UX Improvement",
            "📊 Data Issue",
            "💬 General Feedback"
        ])
        
        feedback_text = st.text_area("Your feedback:", placeholder="Tell us what you think...")
        email = st.text_input("Email (optional):", placeholder="your@email.com")
        
        submitted = st.form_submit_button("🚀 Submit Feedback")
        
        if submitted:
            if feedback_text:
                st.success("✅ Thank you! Your feedback helps us improve.")
                st.balloons()
                
                import datetime
                feedback_data = {
                    "timestamp": datetime.datetime.now().isoformat(),
                    "rating": rating,
                    "type": feedback_type,
                    "feedback": feedback_text,
                    "email": email
                }
                if 'feedback_log' not in st.session_state:
                    st.session_state.feedback_log = []
                st.session_state.feedback_log.append(feedback_data)
            else:
                st.error("Please provide some feedback text.")

# Features list
st.sidebar.markdown("---")
st.sidebar.markdown("### 🌟 **Features**")
st.sidebar.markdown("""
- 🧠 **AI Stress Analysis** (9 factors)
- 🌍 **1000+ Destinations** worldwide  
- 🎒 **Smart Packing Lists** by destination
- 🌤️ **Weather Integration**
- 📊 **Interactive Progress Tracking**
""")

# MAIN CONTENT - Only Travel Stress Predictor (NO DUPLICATES)
display_travel_stress_predictor()

# Footer - MVP Ready with Travel Branding
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px; color: #6c757d;">
    <p>✈️ Built with love for traveling parents everywhere | <strong>MVP Beta Version</strong></p>
    <p style="font-size: 0.9em;">Help us improve by sharing your feedback! 🌍</p>
    <div style="margin-top: 15px;">
        <a href="#" style="color: #3498db; text-decoration: none; margin: 0 10px;">📤 Share on LinkedIn</a>
        <a href="#" style="color: #3498db; text-decoration: none; margin: 0 10px;">💬 Give Feedback</a>
        <a href="#" style="color: #3498db; text-decoration: none; margin: 0 10px;">🌟 Rate This Tool</a>
    </div>
</div>
""", unsafe_allow_html=True)
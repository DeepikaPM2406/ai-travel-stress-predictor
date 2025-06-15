import datetime
import streamlit as st
from agents.travel_comfort_analyzer import display_travel_comfort_analyzer

# ADD THESE NEW IMPORTS:
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_feedback_email(feedback_data):
    """Send feedback via email with UI-visible debugging"""
    try:
        # Email configuration - MAKE SURE THESE ARE YOUR ACTUAL VALUES
        sender_email = "gobabygo.smart@gmail.com"      # Your app's Gmail
        sender_password = "tknporksfajyzpdf"            # Your 16-char app password (no spaces)
        receiver_email = "giri.deepika24@gmail.com"    # Your personal email
        
        # Create message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = f"🍼 GoBabyGo Feedback: {feedback_data['type']}"
        
        # Create email body
        body = f"""
🎉 New feedback received for GoBabyGo!

📅 Timestamp: {feedback_data['timestamp']}
⭐ Rating: {feedback_data['rating']}
📝 Category: {feedback_data['type']}
📧 User Email: {feedback_data['email'] or 'Not provided'}

💬 Feedback Message:
{feedback_data['feedback']}

═══════════════════════════════════════
🍼 Sent from GoBabyGo Smart Travel Companion
✈️ Helping parents travel with confidence!
        """
        
        message.attach(MIMEText(body, "plain"))
        
        # Send email via Gmail SMTP
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        
        return True, "Email sent successfully!"
        
    except smtplib.SMTPAuthenticationError as e:
        return False, f"Gmail login failed: {str(e)}. Check your app password and 2FA settings."
    except smtplib.SMTPRecipientsRefused as e:
        return False, f"Email address rejected: {str(e)}. Check receiver email address."
    except Exception as e:
        return False, f"Email error: {str(e)}"

# Configure the page with GoBabyGo branding
st.set_page_config(
    page_title="GoBabyGo: Smart Travel Companion for Parents",
    page_icon="🍼",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Keep your existing app styling */
    .stApp {
        background: linear-gradient(135deg, #f8f9fa 0%, #e3f2fd 100%);
        font-family: 'Inter', sans-serif;
    }
    
    /* SPECIFIC FIX: Target only those problematic search boxes */
    .stTextInput input,
    div[data-testid="stTextInput"] input,
    input[placeholder*="Search departure"],
    input[placeholder*="Search destination"],
    input[placeholder*="Type to search"],
    input[placeholder*="departure city"],
    input[placeholder*="destination"] {
        background-color: white !important;
        background: white !important;
        color: #2c3e50 !important;
        -webkit-text-fill-color: #2c3e50 !important;
        border: 2px solid #e9ecef !important;
        border-radius: 8px !important;
        padding: 10px 15px !important;
    }
    
    /* Fix only text input placeholder text */
    .stTextInput input::placeholder,
    div[data-testid="stTextInput"] input::placeholder {
        color: #6c757d !important;
        -webkit-text-fill-color: #6c757d !important;
        opacity: 0.8 !important;
    }
    
    /* Keep dropdowns working as they are */
    .stSelectbox > div > div {
        background-color: white !important;
        color: #2c3e50 !important;
        border: 2px solid #e9ecef !important;
        border-radius: 8px !important;
    }
    
    /* Keep multiselect working */
    .stMultiSelect > div > div {
        background-color: white !important;
        color: #2c3e50 !important;
        border: 2px solid #e9ecef !important;
        border-radius: 8px !important;
    }
    
    /* Keep all your existing GoBabyGo branding */
    .gobabygo-header {
        background: linear-gradient(135deg, #ff6b6b 0%, #4ecdc4 50%, #45b7d1 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 800;
        text-align: center;
        margin-bottom: 10px;
        font-size: 2.5rem;
    }
    
    .gobabygo-tagline {
        text-align: center;
        color: #6c757d;
        font-size: 1.2em;
        margin-bottom: 20px;
        font-weight: 500;
    }
    
    .gobabygo-sidebar-title {
        background: linear-gradient(135deg, #ff6b6b 0%, #4ecdc4 50%, #45b7d1 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 800;
    }
    
    .gobabygo-badge {
        background: linear-gradient(135deg, #ff6b6b 0%, #4ecdc4 100%);
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 14px;
        font-weight: 600;
        margin: 10px 0;
        display: inline-block;
    }
    
    /* Keep button styling */
    .stButton > button {
        background: linear-gradient(135deg, #4ecdc4 0%, #45b7d1 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
        padding: 12px 24px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(78, 205, 196, 0.3) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(78, 205, 196, 0.4) !important;
    }
    
    button[kind="primary"] {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%) !important;
        font-size: 18px !important;
        padding: 15px 30px !important;
        box-shadow: 0 4px 15px rgba(255, 107, 107, 0.3) !important;
    }
    
    /* Keep sidebar styling */
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
    
    /* Keep alert styling */
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
    
    /* Keep progress bar */
    .stProgress > div > div > div {
        background: linear-gradient(135deg, #ff6b6b 0%, #4ecdc4 100%) !important;
    }
    
    /* Keep checkbox styling */
    .stCheckbox > label {
        color: #2c3e50 !important;
        font-weight: 500 !important;
    }
    
    /* Keep expander styling */
    .streamlit-expanderHeader {
        background: white !important;
        color: #2c3e50 !important;
        font-weight: 600 !important;
    }
    
    /* Keep card styling */
    .trip-info-card {
        border: 2px solid #4ecdc4;
        border-radius: 12px;
        padding: 20px;
        margin: 15px 0;
        background: linear-gradient(135deg, #4ecdc420 0%, #4ecdc405 100%);
    }
    
    .comfort-score-card {
        border: 2px solid #ff6b6b;
        border-radius: 12px;
        padding: 20px;
        margin: 15px 0;
        background: linear-gradient(135deg, #ff6b6b20 0%, #ff6b6b05 100%);
    }
    
    .product-card {
        border: 2px solid #e9ecef;
        border-radius: 12px;
        padding: 20px;
        background: white;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        height: 100%;
        transition: transform 0.2s ease;
    }
    
    .product-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.15);
    }
    
    .hotel-search-card {
        border: 2px solid #4ecdc4;
        border-radius: 12px;
        padding: 15px;
        margin: 10px 0;
        background: white;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Simple JavaScript to force just the text inputs
st.markdown("""
<script>
function fixSearchBoxes() {
    // Only target text inputs, not dropdowns
    const textInputs = document.querySelectorAll('.stTextInput input, input[placeholder*="Search"], input[placeholder*="Type"]');
    textInputs.forEach(input => {
        if (input.type === 'text' || input.type === 'search') {
            input.style.backgroundColor = 'white';
            input.style.color = '#2c3e50';
            input.style.border = '2px solid #e9ecef';
            input.style.borderRadius = '8px';
        }
    });
}

// Run the fix
setTimeout(fixSearchBoxes, 500);
setTimeout(fixSearchBoxes, 2000);
</script>
""", unsafe_allow_html=True)

# Sidebar Navigation with GoBabyGo branding
st.sidebar.markdown('<h2 class="gobabygo-sidebar-title">🍼 GoBabyGo</h2>', unsafe_allow_html=True)
st.sidebar.markdown("**Smart Travel Companion for Parents**")
st.sidebar.markdown('<div class="gobabygo-badge">🚧 Beta Version</div>', unsafe_allow_html=True)

# FEEDBACK POPUP IMPLEMENTATION - UPDATED WITH DEBUG
if st.sidebar.button("💬 Give Feedback", use_container_width=True):
    with st.sidebar.form("feedback_form"):
        st.markdown("### 📝 Help Us Improve GoBabyGo!")
        
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
            "🏨 Hotel Suggestions",
            "📊 Data Issue",
            "💬 General Feedback"
        ])
        
        feedback_text = st.text_area("Your feedback:", placeholder="Tell us what you think about GoBabyGo...")
        email = st.text_input("Email (optional):", placeholder="your@email.com")
        
        submitted = st.form_submit_button("🚀 Submit Feedback")
        
        if submitted:
            if feedback_text:
                # Show processing message immediately
                with st.spinner("Sending your feedback..."):
                    feedback_data = {
                        "timestamp": datetime.datetime.now().isoformat(),
                        "rating": rating,
                        "type": feedback_type,
                        "feedback": feedback_text,
                        "email": email
                    }
                    
                    # Try to send email with detailed error reporting
                    try:
                        email_success, email_message = send_feedback_email(feedback_data)
                        
                        if email_success:
                            st.success("✅ Thank you! Your feedback has been sent to our team.")
                            st.info(f"📧 {email_message}")
                            st.balloons()
                        else:
                            st.error("❌ Email sending failed:")
                            st.error(f"🔍 {email_message}")
                            st.info("💾 Your feedback is still saved locally as backup.")
                        
                    except Exception as e:
                        st.error("❌ Unexpected error occurred:")
                        st.error(f"🔍 {str(e)}")
                        st.info("💾 Your feedback is still saved locally as backup.")
                    
                    # Always save to session as backup
                    if 'feedback_log' not in st.session_state:
                        st.session_state.feedback_log = []
                    st.session_state.feedback_log.append(feedback_data)
                    
            else:
                st.error("Please provide some feedback text.")

# Features list with GoBabyGo branding
st.sidebar.markdown("---")
st.sidebar.markdown("### 🌟 **Smart Features**")
st.sidebar.markdown("""
- 🧠 **AI Comfort Analysis** (9 factors)
- 🏨 **Dynamic Hotel Search** with filters
- 🌍 **1000+ Destinations** worldwide  
- 🎒 **Smart Packing Lists** with Amazon links
- 🌤️ **Climate-Aware** recommendations
- 📊 **Interactive Progress Tracking**
""")

st.sidebar.markdown("---")
st.sidebar.markdown("### 🎯 **Why GoBabyGo?**")
st.sidebar.markdown("""
- ✅ **Positive approach** - No stress, just comfort
- 🤖 **AI-powered** recommendations
- 👶 **Baby-focused** planning
- 🏨 **Real-time hotel search** with baby filters
- 📱 **Easy to use** interface
""")

# MAIN CONTENT - GoBabyGo Travel Comfort Analyzer
display_travel_comfort_analyzer()

# Footer - GoBabyGo Branding
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px; color: #6c757d;">
    <h3 style="background: linear-gradient(135deg, #ff6b6b 0%, #4ecdc4 50%, #45b7d1 100%); 
               -webkit-background-clip: text; -webkit-text-fill-color: transparent; 
               background-clip: text; font-weight: 800; margin-bottom: 15px;">
        🍼 GoBabyGo: Smart Travel Companion
    </h3>
    <p>✈️ Built with love for traveling parents everywhere | <strong>Beta Version</strong></p>
    <p style="font-size: 0.9em;">Making family travel simple, smart, and enjoyable! 🌍</p>
    <div style="margin-top: 15px;">
        <a href="#" style="color: #ff6b6b; text-decoration: none; margin: 0 10px;">📤 Share GoBabyGo</a>
        <a href="#" style="color: #4ecdc4; text-decoration: none; margin: 0 10px;">💬 Give Feedback</a>
        <a href="#" style="color: #45b7d1; text-decoration: none; margin: 0 10px;">🌟 Rate This Tool</a>
    </div>
    <p style="font-size: 0.8em; margin-top: 15px; color: #999;">
        © 2024 GoBabyGo - Your Smart Travel Companion for Stress-Free Family Adventures
    </p>
</div>
""", unsafe_allow_html=True)
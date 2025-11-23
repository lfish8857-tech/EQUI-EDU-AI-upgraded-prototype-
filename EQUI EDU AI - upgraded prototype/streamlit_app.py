import streamlit as st
from PIL import Image
import io
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import agents
from agents.content_agent import ContentAgent
from agents.assessment_agent import AssessmentAgent
from agents.accessibility_agent import AccessibilityAgent
from agents.equity_agent import EquityAgent
from agents.motivation_agent import MotivationAgent

# Orchestrator
class OrchestratorAgent:
    def __init__(self):
        self.content = ContentAgent()
        self.assessment = AssessmentAgent()
        self.accessibility = AccessibilityAgent()
        self.equity = EquityAgent()
        self.motivation = MotivationAgent()
    
    def handle_request(self, intents, context):
        responses = {}
        
        for intent in intents:
            if intent == "content":
                responses['content'] = self.content.generate(context)
            elif intent == "assessment":
                responses['assessment'] = self.assessment.generate(context)
        
        # Always check accessibility and equity
        if context.get("accessibility") != "none":
            responses['accessibility'] = self.accessibility.make_accessible(context)
        
        responses['equity'] = self.equity.check_fairness(context)
        responses['motivation'] = self.motivation.motivate(context)
        
        return responses

# App Configuration
st.set_page_config(
    page_title="EQUI EDU AI Demo",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 EQUI EDU AI")
st.subheader("Multi-Agent Learning Platform for Educational Equity")

# Initialize orchestrator
if 'orchestrator' not in st.session_state:
    st.session_state.orchestrator = OrchestratorAgent()

# Session Memory
if 'history' not in st.session_state:
    st.session_state.history = []

# Main Form
with st.form("learning_form"):
    st.markdown("### 📋 Tell us about yourself")
    
    col1, col2 = st.columns(2)
    with col1:
        learner = st.text_input("Your Name", placeholder="e.g., Sarah")
    with col2:
        topic = st.text_input("Topic to Learn", placeholder="e.g., Photosynthesis")
    
    col3, col4 = st.columns(2)
    with col3:
        style = st.selectbox("Learning Style", ["simple", "visual", "detailed"])
    with col4:
        accessibility = st.selectbox("Accessibility Need", ["none", "dyslexia", "audio"])
    
    col5, col6 = st.columns(2)
    with col5:
        gender = st.selectbox("Gender", ["female", "male", "other", "prefer not to say"])
    with col6:
        SES = st.selectbox("Socioeconomic Status", ["high", "mid", "low"])
    
    intents = st.multiselect(
        "What would you like?",
        ["content", "assessment"],
        default=["content"]
    )
    
    st.markdown("### 📎 Optional: Upload Media")
    col7, col8 = st.columns(2)
    with col7:
        uploaded_image = st.file_uploader("Picture/Diagram", type=["jpg", "png", "jpeg"])
    with col8:
        uploaded_audio = st.file_uploader("Audio File", type=["mp3", "wav"])
    
    submit = st.form_submit_button("🚀 Get AI Learning Help!", use_container_width=True)

# Process Request
if submit:
    if not topic:
        st.error("Please enter a topic to learn about!")
    else:
        with st.spinner("🤖 AI agents are working..."):
            context = {
                "learner": learner or "Student",
                "topic": topic,
                "style": style,
                "accessibility": accessibility,
                "demographics": {"gender": gender, "SES": SES}
            }
            
            responses = st.session_state.orchestrator.handle_request(intents, context)
            
            # Save to history
            st.session_state.history.append({
                "context": context,
                "responses": responses,
                "image": uploaded_image,
                "audio": uploaded_audio
            })
            
            # Display responses
            st.success("✅ Your personalized learning materials are ready!")
            
            for key, response in responses.items():
                if response:
                    st.markdown("---")
                    st.subheader(f"📌 {key.capitalize()}")
                    
                    # Dyslexia-friendly display
                    if accessibility == "dyslexia" and key in ["content", "assessment"]:
                        st.info("♿ **Dyslexia-Friendly Mode:** Large text with extra spacing for easier reading")
                        
                        st.markdown(
                            """
                            <style>
                            .dyslexia-box {
                                background-color: #FFFEF0;
                                border: 3px solid #FFD700;
                                border-radius: 15px;
                                padding: 30px;
                                margin: 20px 0;
                                font-size: 22px;
                                line-height: 2.5;
                                letter-spacing: 0.1em;
                                font-family: Arial, sans-serif;
                                color: #000000;
                            }
                            </style>
                            """,
                            unsafe_allow_html=True
                        )
                        
                        # Display with HTML escaping to prevent blank pages
                        import html
                        safe_response = html.escape(response)
                        safe_response = safe_response.replace('\n', '<br>')
                        st.markdown(f'<div class="dyslexia-box">{safe_response}</div>', unsafe_allow_html=True)
                    else:
                        st.markdown(response)
            
            # Display uploaded media
            if uploaded_image:
                st.markdown("---")
                st.subheader("📷 Visual Aid")
                st.image(uploaded_image, use_column_width=True)
            
            if uploaded_audio:
                st.markdown("---")
                st.subheader("🔊 Audio Content")
                st.audio(uploaded_audio)

# Session History
if st.session_state.history:
    st.markdown("---")
    st.markdown("## 📚 Session Memory")
    
    for i, entry in enumerate(reversed(st.session_state.history[-3:])):
        with st.expander(f"Session {len(st.session_state.history) - i}: {entry['context']['topic']}"):
            st.write(f"**Learner:** {entry['context']['learner']}")
            st.write(f"**Style:** {entry['context']['style']} | **Accessibility:** {entry['context']['accessibility']}")
            if entry['image']:
                st.write("📷 Image uploaded")
            if entry['audio']:
                st.write("🔊 Audio uploaded")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ for educational equity | Powered by Google Gemini AI")

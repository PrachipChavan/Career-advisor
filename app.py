import streamlit as st
import os
from dotenv import load_dotenv

# Load local environment variables (if any)
load_dotenv()

# Set up page configurations
st.set_page_config(
    page_title="PathFinder AI: Career Advisor",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load and inject custom CSS stylesheet
css_path = os.path.join(os.path.dirname(__file__), "assets", "styles.css")
try:
    with open(css_path, "r") as f:
        css_content = f.read()
        st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)
except Exception as e:
    st.warning(f"Could not load custom styles: {e}")

# Import our custom modules
from modules.assessment import show_assessment
from modules.ai_coach import show_ai_coach
from modules.resume_analyzer import show_resume_analyzer
from modules.roadmap_generator import show_roadmap_generator

# Initialize state management
if "current_page" not in st.session_state:
    st.session_state.current_page = "Dashboard"

if "api_key" not in st.session_state:
    # Read from environment variables if present
    st.session_state.api_key = os.getenv("GROQ_API_KEY", "")

if "selected_model" not in st.session_state:
    st.session_state.selected_model = "llama-3.3-70b-versatile"

# --- SIDEBAR CONFIGURATION ---
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; margin-bottom: 20px;">
        <h2 style="margin:0; font-weight: 800; font-size: 1.8rem; background: linear-gradient(135deg, #00C6FF 0%, #0072FF 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">PathFinder AI</h2>
        <p style="color: rgba(255,255,255,0.6); font-size:0.85rem; margin-top:5px;">Personalized AI Career Ecosystem</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Navigation list
    pages = ["Dashboard", "Career Assessment", "AI Career Coach", "Resume Analyzer", "Skill Roadmap"]
    
    # Simple navigation handling
    selected = st.radio(
        "Navigation Menu:",
        pages,
        index=pages.index(st.session_state.current_page)
    )
    
    # Keep current_page state synced
    if selected != st.session_state.current_page:
        st.session_state.current_page = selected
        st.rerun()
        
    st.markdown("---")
    
    # Secured API key inputs
    st.markdown("### 🔑 API Authentication")
    api_key_input = st.text_input(
        "Enter Groq API Key:",
        type="password",
        value=st.session_state.api_key,
        help="Get an API key from Groq Console (console.groq.com)"
    )
    
    if api_key_input != st.session_state.api_key:
        st.session_state.api_key = api_key_input
        # Set environment variable so our modules can pick it up
        os.environ["GROQ_API_KEY"] = api_key_input
        st.success("API key updated!")
        st.rerun()

    # Model Dropdown Selection
    model_options = ["llama-3.3-70b-versatile", "llama-3.1-8b-instant", "mixtral-8x7b-32768", "gemma2-9b-it"]
    selected_model_input = st.selectbox(
        "Select Groq Model:",
        options=model_options,
        index=model_options.index(st.session_state.selected_model) if st.session_state.selected_model in model_options else 0
    )
    if selected_model_input != st.session_state.selected_model:
        st.session_state.selected_model = selected_model_input
        st.success(f"Switched model to {selected_model_input}!")
        st.rerun()

    # Helpful sidebar guide
    st.markdown("""
    <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.05); padding: 12px; border-radius: 8px; font-size:0.85rem;">
        <strong>How it works:</strong>
        <ol style="margin-top: 5px; padding-left: 20px;">
            <li>Take the <strong>Assessment</strong> to identify matches.</li>
            <li>Consult the <strong>AI Coach</strong> to detail strategies.</li>
            <li>Upload a resume to <strong>Resume Analyzer</strong> to find gaps.</li>
            <li>Build a custom <strong>Skill Roadmap</strong>.</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

# --- DASHBOARD PAGE ---
if st.session_state.current_page == "Dashboard":
    # Top hero section
    st.markdown("""
    <div class="glass-card" style="text-align: center; padding: 40px 20px; background: linear-gradient(135deg, rgba(0, 198, 255, 0.05) 0%, rgba(159, 68, 211, 0.05) 100%) !important;">
        <h1 style="font-size: 3rem; margin: 0; font-weight:800;"><span class="gradient-text-blue">PathFinder AI Career Advisor</span></h1>
        <p style="font-size: 1.2rem; color: rgba(255,255,255,0.7); max-width: 800px; margin: 15px auto;">
            Empower your professional growth. Discover your ideal career path, optimize your resume for ATS tracking, and learn step-by-step with structured roadmap templates.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div style="margin-top:20px;"></div>', unsafe_allow_html=True)
    
    # 4 Quick Links Columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="glass-card" style="height: 220px;">
            <h3>📊 Career Fit Quiz</h3>
            <p style="color: rgba(255,255,255,0.7); font-size:0.95rem;">
                Answer questions about your skills, interests, and working styles to discover career matches based on a dynamic scoring radar.
            </p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Start Assessment", key="nav_quiz"):
            st.session_state.current_page = "Career Assessment"
            st.rerun()
            
        st.markdown("""
        <div class="glass-card" style="height: 220px;">
            <h3>📝 Resume Optimizer</h3>
            <p style="color: rgba(255,255,255,0.7); font-size:0.95rem;">
                Parse your resume PDF and match it with a target job description. Generate ATS scores, extract key missing keywords, and get custom rewrite suggestions.
            </p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Optimize Resume", key="nav_resume"):
            st.session_state.current_page = "Resume Analyzer"
            st.rerun()
            
    with col2:
        st.markdown("""
        <div class="glass-card" style="height: 220px;">
            <h3>💬 AI Chat Coach</h3>
            <p style="color: rgba(255,255,255,0.7); font-size:0.95rem;">
                Get personalized guidance, mock interview support, and custom transition planning in a simulated environment with an AI Career Advisor.
            </p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Consult AI Coach", key="nav_coach"):
            st.session_state.current_page = "AI Career Coach"
            st.rerun()
            
        st.markdown("""
        <div class="glass-card" style="height: 220px;">
            <h3>🗺️ Skill Roadmaps</h3>
            <p style="color: rgba(255,255,255,0.7); font-size:0.95rem;">
                Produce a structured curriculum timeline mapping milestones, skill paths, project goals, and online resources for target job titles.
            </p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Generate Roadmap", key="nav_roadmap"):
            st.session_state.current_page = "Skill Roadmap"
            st.rerun()

# --- OTHER PAGES ROUTING ---
elif st.session_state.current_page == "Career Assessment":
    show_assessment()

elif st.session_state.current_page == "AI Career Coach":
    show_ai_coach()

elif st.session_state.current_page == "Resume Analyzer":
    show_resume_analyzer()

elif st.session_state.current_page == "Skill Roadmap":
    show_roadmap_generator()

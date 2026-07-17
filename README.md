# PathFinder AI: Career Advisor 🎯
<img width="1917" height="895" alt="image" src="https://github.com/user-attachments/assets/6f8b74b2-3e75-4b42-928c-e678b221b255" />

PathFinder AI is a premium, feature-rich Career Advisor dashboard built using **Python**, **Streamlit**, and the **Groq API**. It features a modern, custom glassmorphic dark-theme design and provides four modular tools to help users discover, plan, and optimize their career journeys.

---

## 🌟 Key Features

1. **📊 Career Fit Assessment**
   - Interactive questionnaire covering interests, skills, and values.
   - Dynamic Match Radar Chart powered by **Plotly** to visualize archetype scores (Tech, Business, Healthcare, Creative, Social Impact).
   
2. **💬 AI Career Coach Chat**
   - Context-aware conversation with a virtual Career Advisor powered by Groq LLMs (like `llama-3.3-70b-versatile`).
   - Remembers and utilizes context from your Career Assessment and Resume Analysis to give tailored advice.

3. **📝 Resume Optimization Hub**
   - Upload PDF or TXT resumes and input a target Job Description.
   - Computes an **ATS Match Score** (0-100%).
   - Identifies strengths, key missing keywords, skills gaps, and provides actionable bulleted suggestions.

4. **🗺️ Personalized Skill Roadmaps**
   - Month-by-month study timelines customized to any target career path.
   - Breaks down topics, specific skills to learn, milestones, projects, and free resources.

---

## 🛠️ Tech Stack & Dependencies

* **Frontend/Core**: [Streamlit](https://streamlit.io/)
* **AI Provider**: [Groq Cloud SDK](https://console.groq.com/)
* **Charts/Visuals**: [Plotly](https://plotly.com/)
* **Document Parsing**: [pdfplumber](https://github.com/jsvine/pdfplumber)
* **Environment/Config**: `python-dotenv`

---

## 🚀 Installation & Setup

### 1. Clone or Download the Project
Make sure the project structure looks like this:
```text
career_advisor/
├── app.py
├── requirements.txt
├── README.md
├── assets/
│   └── styles.css
└── modules/
    ├── assessment.py
    ├── ai_coach.py
    ├── resume_analyzer.py
    └── roadmap_generator.py
```

### 2. Install Dependencies
It is highly recommended to use a virtual environment:
```bash
# Create a virtual environment
python -m venv .venv

# Activate it (Windows PowerShell)
.venv\Scripts\Activate.ps1

# Activate it (macOS/Linux)
source .venv/bin/activate

# Install the required packages
pip install -r requirements.txt
```

### 3. Add API Key
Get a Groq API Key from the [Groq Console](https://console.groq.com/). You can either:
- Set it as an environment variable in your terminal:
  ```bash
  # Windows PowerShell
  $env:GROQ_API_KEY="your-api-key-here"

  # macOS/Linux or Git Bash
  export GROQ_API_KEY="your-api-key-here"
  ```
- Or paste it directly in the running app's secure sidebar.

### 4. Launch the App
Run the Streamlit application:
```bash
streamlit run app.py
```
Open the provided URL (usually `http://localhost:8501`) in your browser to start planning!

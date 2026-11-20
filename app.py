import os
import json
import streamlit as st

# Load environment variables if available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# ==========================================
# PAGE CONFIGURATION & STYLING
# ==========================================
st.set_page_config(
    page_title="AI Career Roadmap & Skill Gap Finder",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern UI design
st.markdown("""
<style>
    .main-title {
        font-size: 2.2rem;
        font-weight: 800;
        color: #1E3A8A;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        font-size: 1.05rem;
        color: #4B5563;
        margin-bottom: 1.5rem;
    }
    .week-card {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-left: 5px solid #2563EB;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 14px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.04);
    }
    .week-header {
        font-size: 1.05rem;
        font-weight: 700;
        color: #1E3A8A;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .milestone-badge {
        display: inline-block;
        background-color: #EFF6FF;
        color: #1D4ED8;
        font-size: 0.8rem;
        font-weight: 600;
        padding: 4px 10px;
        border-radius: 12px;
        border: 1px solid #BFDBFE;
        margin-top: 8px;
    }
    .project-card {
        background: linear-gradient(135deg, #F8FAFC 0%, #EFF6FF 100%);
        border: 1px solid #DBEAFE;
        border-radius: 10px;
        padding: 18px;
        height: 100%;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
    }
    .project-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #1E40AF;
        margin-bottom: 6px;
    }
    .tech-pill {
        display: inline-block;
        background-color: #DBEAFE;
        color: #1E40AF;
        padding: 2px 8px;
        border-radius: 12px;
        font-size: 0.75rem;
        font-weight: 600;
        margin-right: 4px;
        margin-top: 4px;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# SIDEBAR CONFIGURATION
# ==========================================
with st.sidebar:
    st.image("https://img.icons8.com/color/96/compass--v1.png", width=64)
    st.title("Career Settings")
    st.markdown("Configure your AI model settings & presets.")
    
    # Check for GEMINI_API_KEY
    env_key = os.getenv("GEMINI_API_KEY", "")
    if not env_key and "GEMINI_API_KEY" in st.secrets:
        env_key = st.secrets["GEMINI_API_KEY"]
        
    api_key = st.text_input(
        "Google Gemini API Key",
        value=env_key,
        type="password",
        help="Get your free API key at https://aistudio.google.com/"
    )
    
    use_demo_mode = st.checkbox(
        "🧪 Test with Demo Mode (Mock AI)", 
        value=(not api_key),
        help="Check this to test the app without an API key."
    )
    
    st.divider()
    st.markdown("### Quick Presets")
    preset_choice = st.selectbox(
        "Select an Example Goal:",
        ["Custom Input", "Fresher to Data Scientist", "Web Beginner to Full Stack Dev", "Student to Cloud / DevOps Engineer"]
    )
    
    st.divider()
    st.markdown("""
    ### How it works:
    1. Enter your **Current Skills**.
    2. Enter your **Target Job Role**.
    3. Choose your **Weekly Study Hours**.
    4. Click **Generate 8-Week Roadmap**!
    """)
    st.caption("AI Career Roadmap & Skill Gap Finder • Task 2")

# Preset values
default_skills = "C, basic Python, HTML, Git, basic SQL"
default_role = "Data Scientist"
default_hours = 12

if preset_choice == "Fresher to Data Scientist":
    default_skills = "C programming, basic Python, linear algebra, Excel, HTML"
    default_role = "Data Scientist"
    default_hours = 15
elif preset_choice == "Web Beginner to Full Stack Dev":
    default_skills = "HTML, CSS, basic JavaScript, Git"
    default_role = "Full Stack Web Developer"
    default_hours = 12
elif preset_choice == "Student to Cloud / DevOps Engineer":
    default_skills = "Linux basics, Python scripting, Git, basic networking"
    default_role = "Cloud / DevOps Engineer"
    default_hours = 10

# ==========================================
# HELPER FUNCTIONS & AI MODEL CALL
# ==========================================
def call_gemini_roadmap(api_key: str, current_skills: str, target_role: str, hours_per_week: int) -> dict:
    """Calls Google Gemini to perform skills gap analysis and generate an 8-week plan."""
    prompt = f"""
You are an expert Career Counselor and Senior Tech Industry Mentor.
A student wants to transition into the target job role of '{target_role}'.

Candidate Profile:
- Current Skills: {current_skills}
- Target Job Role: {target_role}
- Time Commitment: {hours_per_week} hours per week for 8 weeks

Perform a comprehensive Skill Gap Analysis and build a structured, week-by-week 8-week learning plan and 3 mini project ideas for their portfolio.

Respond strictly with a valid JSON object matching this schema:
{{
    "summary": "<2-sentence encouragement and strategy overview>",
    "skills_have": ["<skill 1>", "<skill 2>", ...],
    "skills_to_learn": [
        {{"skill": "<missing skill 1>", "importance": "High", "why": "<brief reason>"}},
        {{"skill": "<missing skill 2>", "importance": "Medium", "why": "<brief reason>"}},
        ...
    ],
    "roadmap": [
        {{
            "week": 1,
            "title": "<Week 1 Title / Theme>",
            "topics": ["<Topic 1>", "<Topic 2>", "<Topic 3>"],
            "milestone": "<End-of-week tangible achievement>"
        }},
        ... (generate exactly 8 weeks, week 1 through 8)
    ],
    "mini_projects": [
        {{
            "title": "<Project 1 Title>",
            "description": "<2-sentence project overview suitable for resume/portfolio>",
            "skills_used": ["<Skill A>", "<Skill B>", "<Skill C>"]
        }},
        {{
            "title": "<Project 2 Title>",
            "description": "<2-sentence project overview suitable for resume/portfolio>",
            "skills_used": ["<Skill A>", "<Skill B>"]
        }},
        {{
            "title": "<Project 3 Title>",
            "description": "<2-sentence project overview suitable for resume/portfolio>",
            "skills_used": ["<Skill A>", "<Skill B>", "<Skill C>"]
        }}
    ]
}}

Return raw JSON only. Do not wrap in markdown or backticks.
"""

    response_text = None
    # 1. Try google-genai SDK
    try:
        from google import genai
        client = genai.Client(api_key=api_key)
        for model_name in ['gemini-2.0-flash', 'gemini-1.5-flash']:
            try:
                response = client.models.generate_content(
                    model=model_name,
                    contents=prompt,
                )
                response_text = response.text
                if response_text:
                    break
            except Exception:
                continue
    except Exception:
        pass

    # 2. Fallback to google-generativeai SDK
    if not response_text:
        try:
            import google.generativeai as genai_legacy
            genai_legacy.configure(api_key=api_key)
            for model_name in ['gemini-1.5-flash', 'gemini-1.5-pro']:
                try:
                    model = genai_legacy.GenerativeModel(model_name)
                    response = model.generate_content(prompt)
                    response_text = response.text
                    if response_text:
                        break
                except Exception:
                    continue
        except Exception:
            raise RuntimeError("Gemini API request failed. Please check your API key.")

    if not response_text:
        raise RuntimeError("No response returned from Gemini API. Please check your API key.")

    # Parse JSON reliably
    start_idx = response_text.find('{')
    end_idx = response_text.rfind('}')
    if start_idx != -1 and end_idx != -1:
        json_str = response_text[start_idx:end_idx+1]
        return json.loads(json_str)
    else:
        return json.loads(response_text.strip())

def get_mock_roadmap(current_skills: str, target_role: str, hours_per_week: int) -> dict:
    """Provides high-quality realistic fallback data for demo and offline evaluation."""
    return {
        "summary": f"With {hours_per_week} hours per week, you can bridge the gap from your current foundation to becoming a junior {target_role} in 8 focused weeks.",
        "skills_have": [
            "C Programming (Foundational Logic)",
            "Basic Python Syntax",
            "HTML & Web Basics",
            "Git Version Control",
            "Basic SQL Queries"
        ],
        "skills_to_learn": [
            {"skill": "Advanced Pandas & NumPy", "importance": "High", "why": "Essential for data manipulation and preprocessing."},
            {"skill": "Statistical Analysis & Probability", "importance": "High", "why": "Core mathematical theory behind machine learning models."},
            {"skill": "Scikit-Learn (Supervised/Unsupervised ML)", "importance": "High", "why": "Standard industry toolkit for building ML models."},
            {"skill": "Data Visualization (Seaborn, Matplotlib)", "importance": "Medium", "why": "Communicating insights effectively to stakeholders."},
            {"skill": "Model Evaluation & Metrics (ROC-AUC, RMSE)", "importance": "Medium", "why": "Verifying model performance on real test datasets."},
            {"skill": "Model Deployment (Streamlit / FastAPI)", "importance": "Medium", "why": "Showcasing live models in your portfolio."}
        ],
        "roadmap": [
            {
                "week": 1,
                "title": "Week 1: Advanced Python for Data & Math Foundations",
                "topics": ["List comprehensions & lambda functions", "NumPy array vectorization & linear algebra", "Matrix operations & statistics"],
                "milestone": "Build 5 NumPy computation scripts solving statistical problems."
            },
            {
                "week": 2,
                "title": "Week 2: Data Wrangling & Cleaning with Pandas",
                "topics": ["DataFrame indexing & filtering", "Handling missing values & duplicates", "GroupBy aggregations & merging datasets"],
                "milestone": "Clean and explore an messy real-world CSV dataset from Kaggle."
            },
            {
                "week": 3,
                "title": "Week 3: Exploratory Data Analysis (EDA) & Visualization",
                "topics": ["Matplotlib & Seaborn chart aesthetics", "Correlation heatmaps & outlier detection", "Feature distribution analysis"],
                "milestone": "Produce a complete EDA notebook with 8 visual charts and business insights."
            },
            {
                "week": 4,
                "title": "Week 4: Classical Machine Learning - Regression",
                "topics": ["Linear & Ridge/Lasso Regression", "Train-test split & cross-validation", "Evaluation: MAE, MSE, and R-squared"],
                "milestone": "Train a House Price Prediction model with R-squared > 0.85."
            },
            {
                "week": 5,
                "title": "Week 5: Classification Algorithms & Metrics",
                "topics": ["Logistic Regression & Decision Trees", "Random Forests & Ensemble basics", "Confusion Matrix, Precision, Recall, F1"],
                "milestone": "Implement a Customer Churn Classifier with full classification report."
            },
            {
                "week": 6,
                "title": "Week 6: Unsupervised Learning & Feature Engineering",
                "topics": ["K-Means Clustering & PCA dimensionality reduction", "Categorical encoding (One-Hot, Ordinal)", "Feature scaling (MinMax, StandardScaler)"],
                "milestone": "Segment customer transaction data into 4 distinct persona clusters."
            },
            {
                "week": 7,
                "title": "Week 7: Capstone Project & Model Serving",
                "topics": ["Model serialization with joblib/pickle", "Building a Streamlit UI for user inference", "Testing edge cases and validation"],
                "milestone": "Deploy a working end-to-end interactive machine learning web app."
            },
            {
                "week": 8,
                "title": "Week 8: Portfolio Polish & Interview Preparation",
                "topics": ["Writing clear README with project architecture", "Pushing clean GitHub repos", "Common ML behavioral & technical interview Q&A"],
                "milestone": "Host 3 live portfolio projects with complete documentation on GitHub."
            }
        ],
        "mini_projects": [
            {
                "title": "1. E-Commerce Customer Churn Predictor",
                "description": "Predict whether a customer will cancel their subscription based on usage patterns. Built with Scikit-learn and deployed with a Streamlit interface.",
                "skills_used": ["Python", "Pandas", "Scikit-Learn", "Streamlit", "ROC-AUC"]
            },
            {
                "title": "2. Real Estate Price Estimator with EDA",
                "description": "An interactive regression model that estimates housing values based on square footage, location, and amenities, with interactive data visualizations.",
                "skills_used": ["NumPy", "Pandas", "Seaborn", "Linear Regression", "Feature Engineering"]
            },
            {
                "title": "3. Credit Card Fraud Detection Pipeline",
                "description": "An anomaly detection and classification pipeline handling highly imbalanced transaction data using SMOTE and Random Forest.",
                "skills_used": ["Scikit-Learn", "Imbalanced Data", "Confusion Matrix", "Git", "Model Evaluation"]
            }
        ]
    }

# ==========================================
# MAIN INTERFACE
# ==========================================
st.markdown('<div class="main-title">🧭 AI Career Roadmap & Skill Gap Finder</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Bridge the gap between your current skills and your dream job role with an AI-generated 8-week learning plan.</div>', unsafe_allow_html=True)

# Input Row (Columns)
col1, col2, col3 = st.columns([2, 2, 1], gap="medium")

with col1:
    st.subheader("1. Current Skills")
    current_skills_input = st.text_area(
        "List skills, programming languages, or tools you know:",
        value=default_skills,
        height=120,
        placeholder="e.g. C, basic Python, HTML, Git, basic SQL"
    )

with col2:
    st.subheader("2. Target Job Role")
    target_role_input = st.text_input(
        "Enter your desired job title:",
        value=default_role,
        placeholder="e.g. Data Scientist, Full Stack Developer, DevOps Engineer"
    )
    st.caption("Tip: Be as specific as possible (e.g. 'Backend Python Developer' or 'Data Scientist').")

with col3:
    st.subheader("3. Study Time")
    hours_input = st.slider(
        "Hours per week available:",
        min_value=4,
        max_value=40,
        value=default_hours,
        step=2,
        help="How many hours can you dedicate each week?"
    )
    st.info(f"⏱️ **{hours_input * 8} total hours** over 8 weeks")

# Action Button
st.markdown("<br>", unsafe_allow_html=True)
btn_col1, btn_col2, btn_col3 = st.columns([1, 2, 1])
with btn_col2:
    generate_clicked = st.button("🚀 Generate 8-Week Roadmap & Skill Gap", use_container_width=True, type="primary")

# ==========================================
# RESULTS DISPLAY
# ==========================================
if generate_clicked:
    if not current_skills_input.strip():
        st.error("⚠️ Please specify at least one current skill.")
    elif not target_role_input.strip():
        st.error("⚠️ Please enter your target job role.")
    else:
        roadmap_data = None
        
        # Demo mode or live API
        if use_demo_mode or not api_key:
            if not api_key and not use_demo_mode:
                st.warning("⚠️ No Gemini API key provided. Running in Demo Mode (Mock AI). Add your API key in the sidebar for live Gemini output.")
            with st.spinner("Analyzing skill gaps and structuring your 8-week roadmap (Demo Mode)..."):
                roadmap_data = get_mock_roadmap(current_skills_input, target_role_input, hours_input)
        else:
            with st.spinner(f"🤖 Gemini AI is creating a customized 8-week plan for '{target_role_input}'..."):
                try:
                    roadmap_data = call_gemini_roadmap(api_key, current_skills_input, target_role_input, hours_input)
                except Exception as ex:
                    st.error(f"AI generation failed: {ex}")
                    st.info("Switching to Demo Mode output so you can preview the roadmap:")
                    roadmap_data = get_mock_roadmap(current_skills_input, target_role_input, hours_input)

        if roadmap_data:
            st.divider()
            st.header("🎯 Your Personalized Career Strategy")
            
            summary = roadmap_data.get("summary", "")
            if summary:
                st.success(f"💡 **Strategy Overview:** {summary}")

            # ------------------------------------------
            # 1. SKILLS GAP ANALYSIS TABLE
            # ------------------------------------------
            st.markdown("### 📊 1. Skill Gap Analysis: What You Have vs What to Learn")
            
            gap_col1, gap_col2 = st.columns(2)
            
            with gap_col1:
                st.subheader("✅ Skills You Already Have")
                have_list = roadmap_data.get("skills_have", [])
                if have_list:
                    for s in have_list:
                        st.markdown(f"- **{s}**")
                else:
                    st.write("Starting fresh from foundational concepts.")

            with gap_col2:
                st.subheader("🎯 Critical Skills You Need to Learn")
                learn_list = roadmap_data.get("skills_to_learn", [])
                
                # Format into a clean table
                if learn_list:
                    table_rows = []
                    for item in learn_list:
                        if isinstance(item, dict):
                            skill_name = item.get("skill", "")
                            prio = item.get("importance", "High")
                            why = item.get("why", "")
                            table_rows.append({"Skill to Learn": skill_name, "Priority": prio, "Why It Matters": why})
                        else:
                            table_rows.append({"Skill to Learn": str(item), "Priority": "High", "Why It Matters": "Required for role"})
                    st.table(table_rows)

            st.divider()

            # ------------------------------------------
            # 2. 8-WEEK WEEK-BY-WEEK ROADMAP
            # ------------------------------------------
            st.markdown(f"### 🗓️ 2. Week-by-Week Learning Roadmap ({hours_input} hrs/week)")
            
            weeks = roadmap_data.get("roadmap", [])
            
            # Show in 2 columns of 4 weeks each
            w_col1, w_col2 = st.columns(2)
            
            for idx, w in enumerate(weeks):
                col_target = w_col1 if idx % 2 == 0 else w_col2
                with col_target:
                    w_num = w.get("week", idx + 1)
                    w_title = w.get("title", f"Week {w_num}")
                    w_topics = w.get("topics", [])
                    w_milestone = w.get("milestone", "Complete weekly assignment.")
                    
                    st.markdown(f"""
                    <div class="week-card">
                        <div class="week-header">
                            <span>📅</span> {w_title}
                        </div>
                        <ul style="margin-top: 8px; margin-bottom: 8px; font-size: 0.9rem; padding-left: 20px;">
                            {''.join([f'<li>{t}</li>' for t in w_topics])}
                        </ul>
                        <div class="milestone-badge">
                            🏁 <strong>Weekly Milestone:</strong> {w_milestone}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

            st.divider()

            # ------------------------------------------
            # 3. 3 PORTFOLIO MINI PROJECT IDEAS
            # ------------------------------------------
            st.markdown("### 🛠️ 3. Portfolio Mini Project Ideas")
            st.markdown("Build these 3 projects to prove your hands-on ability to recruiters:")

            p_cols = st.columns(3)
            projects = roadmap_data.get("mini_projects", [])
            for p_idx, proj in enumerate(projects[:3]):
                with p_cols[p_idx]:
                    p_title = proj.get("title", f"Project #{p_idx+1}")
                    p_desc = proj.get("description", "")
                    p_skills = proj.get("skills_used", [])
                    
                    pills_html = "".join([f'<span class="tech-pill">{s}</span>' for s in p_skills])
                    
                    st.markdown(f"""
                    <div class="project-card">
                        <div class="project-title">{p_title}</div>
                        <p style="font-size: 0.88rem; color: #334155; margin-bottom: 12px;">{p_desc}</p>
                        <div>{pills_html}</div>
                    </div>
                    """, unsafe_allow_html=True)

            # ------------------------------------------
            # DOWNLOAD BUTTON
            # ------------------------------------------
            st.markdown("<br>", unsafe_allow_html=True)
            
            report_lines = [
                f"=== AI CAREER ROADMAP & SKILL GAP REPORT ===",
                f"Target Job Role: {target_role_input}",
                f"Current Skills: {current_skills_input}",
                f"Study Commitment: {hours_input} Hours/Week (8-Week Total: {hours_input * 8} Hours)",
                f"\n--- STRATEGY SUMMARY ---",
                summary,
                f"\n--- SKILLS YOU ALREADY HAVE ---",
                "\n".join([f"✓ {s}" for s in have_list]),
                f"\n--- SKILLS TO LEARN ---",
            ]
            for item in learn_list:
                if isinstance(item, dict):
                    report_lines.append(f"• {item.get('skill')} [{item.get('importance')}] - {item.get('why')}")
                else:
                    report_lines.append(f"• {item}")

            report_lines.append("\n--- 8-WEEK ROADMAP ---")
            for w in weeks:
                report_lines.append(f"\n{w.get('title')}:")
                for t in w.get("topics", []):
                    report_lines.append(f"  - {t}")
                report_lines.append(f"  Milestone: {w.get('milestone')}")

            report_lines.append("\n--- 3 PORTFOLIO MINI PROJECTS ---")
            for p in projects:
                report_lines.append(f"\n* {p.get('title')}")
                report_lines.append(f"  Description: {p.get('description')}")
                report_lines.append(f"  Skills: {', '.join(p.get('skills_used', []))}")

            roadmap_text = "\n".join(report_lines)

            st.download_button(
                label="📥 Download Full Roadmap (.txt)",
                data=roadmap_text,
                file_name=f"{target_role_input.replace(' ', '_')}_8Week_Roadmap.txt",
                mime="text/plain",
                use_container_width=True
            )
            st.balloons()

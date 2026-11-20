# 🧭 AI Career Roadmap & Skill Gap Finder
> **Task 2: Prototype or Model Creation using AI**  
> **Problem Statement #4:** AI Career Roadmap & Skill Gap Finder  
> **Tech Stack:** Python (Streamlit) / HTML+JavaScript + Google Gemini API  

---

## 📌 1. Problem Overview
Many university students and early-career engineers know the job title they aspire to achieve (e.g., Data Scientist, Full Stack Developer, DevOps Engineer), but struggle to determine **what to learn, in what chronological order, and how to allocate their study hours**.

This prototype provides an end-to-end personalized learning plan:
1. **Inputs:**
   - **Current Skills:** (e.g., C, basic Python, HTML, basic SQL)
   - **Target Job Role:** (e.g., Data Scientist)
   - **Hours per week available to study:** (e.g., 10–15 hrs/week)
2. **AI Processing:**
   - Google Gemini evaluates the delta between the student's current skills and current industry requirements.
3. **Outputs:**
   - **Skills Gap Analysis Table:** Skills Already Have vs. Skills to Learn (categorized by High/Medium priority with explanations).
   - **8-Week Learning Roadmap:** Week-by-week syllabus featuring specific topics and concrete end-of-week milestones.
   - **3 Portfolio Mini Projects:** Real-world project ideas with descriptions and tech stack tags to build an impressive GitHub portfolio.
   - **Downloadable Report:** Complete roadmap in clean `.txt` format.

---

## 📂 2. Project Structure
```text
ai_career_roadmap/
├── app.py                 # Streamlit web application (Python)
├── index.html             # Standalone web application (HTML5 + CSS3 + JS)
├── requirements.txt       # Python dependencies (streamlit, google-genai, etc.)
├── .env.example           # Template for storing GEMINI_API_KEY safely
├── .gitignore             # Excludes secret keys (.env) and virtual environments
├── README.md              # Project documentation and setup guide
├── EXPLANATION.md         # Comprehensive Viva / Oral Evaluation Guide
├── package_submission.ps1 # One-click script to generate submission ZIP
└── Sample_RollNo_Name_Code.zip # Pre-packaged ready-to-submit archive
```

---

## 🚀 3. How to Run the Prototype

### Option A: Python + Streamlit (Recommended for Python evaluation)
1. **Open Command Prompt / Terminal** in this directory:
   ```bash
   cd C:\Users\prade\.gemini\antigravity\scratch\ai_career_roadmap
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run Streamlit:**
   ```bash
   streamlit run app.py
   ```
4. Enter your Gemini API key in the sidebar, or simply check **🧪 Test with Demo Mode**.

---

### Option B: Standalone Web App (Zero-Setup Instant Demo)
1. Simply double-click [`index.html`](file:///C:/Users/prade/.gemini/antigravity/scratch/ai_career_roadmap/index.html) to open in **Chrome, Edge, or Opera**.
2. Select a preset (e.g. *Fresher to Data Scientist*) or type your custom skills.
3. Click **🚀 Generate 8-Week Roadmap & Skill Gap**.

---

## 🔑 4. Getting a Free Google Gemini API Key
1. Go to [Google AI Studio](https://aistudio.google.com/).
2. Click **Get API key** -> **Create API key**.
3. Paste the key into the app's sidebar, or create a `.env` file:
   ```env
   GEMINI_API_KEY=AIzaSyYourKeyHere
   ```

---

## 📸 5. How to Submit (Google Form Checklist)

### 1. Code ZIP File (`RollNo_Name_Code.zip`)
Run the helper script in PowerShell:
```powershell
.\package_submission.ps1 -RollNo "YOUR_ROLL_NO" -Name "YOUR_NAME"
```
*(This ensures your private `.env` key is NOT included in the submission ZIP, complying with the rubric).*

### 2. Screenshot (`RollNo_Name_Output.jpg` or `.png`)
- Run the app, click **Generate**, and take a clean screenshot showing:
  - Skills Gap Table (Have vs. To Learn)
  - 8-Week Roadmap Cards
  - 3 Mini Project Ideas
- Name the screenshot: `RollNo_Name_Output.jpg` (e.g. `21CS045_RahulSharma_Output.jpg`).

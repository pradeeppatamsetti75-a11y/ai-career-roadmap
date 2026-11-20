# 🎓 Viva & Code Explanation Guide
## Problem Statement 4: AI Career Roadmap & Skill Gap Finder

Use this guide to confidently explain your project during viva, presentation, or practical exam evaluation.

---

### 1. Project Overview & Motivation
**Question:** *What problem does your application address?*  
**Answer:**  
"Students often know the job title they want to land (e.g. Data Scientist, Cloud Engineer, Full Stack Developer), but they suffer from information overload. They don't know what skills they need, which prerequisites to learn first, or how to pace their studies with limited time.  
Our application takes the student's current skill profile, target role, and weekly time commitment, and uses Google Gemini to compute:
1. A **Skills Gap Analysis** differentiating existing capabilities from missing industry requirements.
2. An **8-Week Chronological Roadmap** with weekly milestones.
3. **3 Portfolio Mini Projects** designed to prove their practical competence to recruiters."

---

### 2. How the AI Pipeline Works
**Question:** *How is the AI model integrated into the application?*  
**Answer:**  
The workflow follows a 3-step pattern:
1. **User Input:**
   - Current skills: string of languages, tools, frameworks.
   - Target job role: desired employment title.
   - Weekly commitment: 4 to 40 hours per week.
2. **AI Reasoning (Gemini Prompt Engineering):**
   - The system prompt defines Gemini's persona as an *Expert Career Counselor and Tech Industry Mentor*.
   - It supplies the student's constraints and enforces a strict, validated **JSON schema**.
   - Gemini calculates the gap, schedules the 8-week syllabus tailored to the student's hours, and crafts 3 mini projects.
3. **Frontend Rendering:**
   - The JSON response is parsed into clean Python dictionaries (or JS objects).
   - The skills gap is formatted into a comparison table.
   - The 8-week roadmap is mapped to visual weekly cards with milestone badges.
   - The 3 mini projects are displayed with technology pills and portfolio descriptions.

---

### 3. Key Code Highlights

#### A. Prompt Engineering & JSON Schema Enforcement
```python
prompt = f"""
You are an expert Career Counselor and Senior Tech Industry Mentor.
A student wants to transition into the target job role of '{target_role}'.

Candidate Profile:
- Current Skills: {current_skills}
- Target Job Role: {target_role}
- Time Commitment: {hours_per_week} hours per week for 8 weeks

Perform a comprehensive Skill Gap Analysis and build a structured, week-by-week 8-week learning plan and 3 mini project ideas for their portfolio.
Respond strictly with a valid JSON object matching this schema:
...
"""
```
- **Why JSON?** Instead of returning unformatted paragraphs of text, requesting structured JSON ensures our UI can dynamically render tables, cards, and tags.

#### B. Robust JSON Extraction
```python
start_idx = response_text.find('{')
end_idx = response_text.rfind('}')
if start_idx != -1 and end_idx != -1:
    json_str = response_text[start_idx:end_idx+1]
    return json.loads(json_str)
```
- **Why this logic?** LLMs sometimes enclose responses in markdown blocks (e.g., ```` ```json ... ``` ````). By extracting from the first `{` to the last `}`, the code never crashes on markdown code fences or greeting text.

#### C. Built-in Demo Mode Fallback
- Enables instantaneous presentation and offline grading even if the testing computer lacks an internet connection or Gemini API credentials.

---

### 4. Common Viva Questions & Model Answers

**Q1: How does the model adapt to different study hours?**  
*Answer:* The prompt explicitly passes `Time Commitment: {hours_per_week} hours per week`. For a 10 hrs/week schedule, the model scopes weekly topics to foundational milestones; for 30 hrs/week, it introduces deeper system internals and advanced frameworks.

**Q2: How is user data kept secure?**  
*Answer:* The API key is never hardcoded. It is read from `.env` or temporary session memory. The `.gitignore` file specifically prevents sensitive `.env` files from being bundled into git commits or submission ZIP archives.

**Q3: What are the benefits of Streamlit for this app?**  
*Answer:* Streamlit provides rapid reactive UI development in pure Python (`st.slider`, `st.columns`, `st.table`, `st.download_button`) without the overhead of maintaining a separate backend server.

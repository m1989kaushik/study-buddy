import os
import streamlit as st
import google.generativeai as genai
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")
# Client initialize karna
genai.configure(api_key="AQ.Ab8RN6L9kx9eITiO6WJFdrI1c3_OPPn1KcRIk9qjkDmP78OvaA")
model = genai.GenerativeModel("gemini-1.5-flash")
st.set_page_config(page_title="AI Study Buddy", layout="centered")

st.title("📚 AI Doubt Solver (Class 9-12)")
st.caption("फोटो खींचो या सवाल लिखो - तुरंत स्टेप-बाय-स्टेप समाधान पाओ")

# अपनी Gemini API Key यहाँ डालें
API_KEY = "AQ.Ab8RN6KtshouqldoNr-c4F0wi1vw5XKa4vkoM2EfZH_3iJABoA"

col1, col2 = st.columns(2)
with col1:
    std_class = st.selectbox("कक्षा:", ["Class 9", "Class 10", "Class 11", "Class 12"])
with col2:
    subject = st.selectbox("विषय:", ["Mathematics", "Science / Physics", "Chemistry", "Biology"])

uploaded_file = st.file_uploader("सवाल की फोटो अपलोड करें (वैकल्पिक):", type=["jpg", "jpeg", "png"])
if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="अपलोड की गई फोटो", width=300)

user_question = st.text_area("या फिर सवाल यहाँ टाइप करें:", height=100)

if st.button("सॉल्यूशन दिखाओ 🚀"):
    if not user_question.strip() and not uploaded_file:
        st.warning("कृपया सवाल लिखें या फोटो अपलोड करें!")
    elif API_KEY == "YOUR_GEMINI_API_KEY_HERE":
        st.error("कृपया कोड में अपनी असली Gemini API Key डालें!")
    else:
        with st.spinner("AI शिक्षक हल तैयार कर रहा है..."):
            prompt = f"""
            You are an expert CBSE/State board tutor for {std_class} teaching {subject}.
            Solve the user's doubt step-by-step with clear explanations.

            Analyze the provided question: "{user_question}".
            Rules:
            1. Language: Simple Hinglish (Hindi + English).
            2. Steps: Clear, step-by-step exam-oriented solution.
            3. Highlight key formulas and common mistakes students make.
            """

            contents = [prompt]
            if uploaded_file:
            contents.append(img)

            response = model.generate_content(contents)

            st.success("समाधान:")
            st.markdown(response.text)

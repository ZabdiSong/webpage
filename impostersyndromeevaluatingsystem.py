import streamlit as st

# --- QUESTIONS AND SCALE ---
questions = {
    "Low Self-Esteem": [
        "I feel unworthy of my accomplishments, no matter how much I’ve achieved.",
        "I downplay my successes or attribute them to luck.",
        "I feel like others have been deceived into thinking I’m more competent than I really am.",
    ],
    "Depression and Anxiety": [
        "I feel helpless or overwhelmed even when meeting expectations.",
        "I often experience intense negative feelings related to my work or performance.",
        "I feel stressed or anxious when I’m acknowledged or praised.",
    ],
    "Upbringing and Parenting Style": [
        "My caregivers rarely praised or encouraged me when I was a child.",
        "I was only praised when I achieved something.",
        "I felt like approval was conditional on success.",
    ],
    "Social Media": [
        "I feel pressure to keep up with the perfect lives shown on social media.",
        "I compare my achievements with others online.",
        "I rely on online feedback or validation to feel good about myself.",
    ],
    "Being Different from Peers": [
        "Do you feel disconnected or out of place among your peers, even in familiar settings?",
        "How often do you question your achievements because you feel different from others?",
        "Do you find it hard to relate to others in your academic or professional environment due to personal differences?"
    ],
    "Academia / Working Atmosphere": [
        "Does the competitive or high-pressure environment at work or school make you question your capabilities?",
        "How often do you feel like you're falling behind your peers or colleagues?",
        "Do you experience stress when trying to meet the expectations of your institution or workplace?"
    ],
    "Perfectionism": [
        "Do you feel that even the smallest flaw in your work means complete failure?",
        "How often are you afraid of making mistakes, even when learning something new?",
        "When something doesn’t go perfectly, do you dwell on it or see it as a reflection of your worth?"
    ],
    "Stereotypes": [
        "Do you feel your achievements are overlooked or diminished because of assumptions about your identity (e.g., gender, race, background)?",
        "Have you ever felt that your success was attributed to tokenism rather than your own merit?",
        "Do stereotypes in your environment affect how confident you feel in your abilities?"
    ]
}

scale = {
    "Strongly Disagree": 1,
    "Disagree": 2,
    "Neutral": 3,
    "Agree": 4,
    "Strongly Agree": 5
}

# --- INIT SESSION STATE ---
if 'responses' not in st.session_state:
    st.session_state.responses = {}
if 'ensured' not in st.session_state:
    st.session_state.ensured = {}
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False

# --- CALCULATE TOTALS ---
total_questions = sum(len(q_list) for q_list in questions.values())
ensured_count = len(st.session_state.ensured)
progress_percent = int((ensured_count / total_questions) * 100)

# --- DISPLAY HEADER AND PROGRESS ---
st.title("Imposter Syndrome Evaluating System")
st.progress(progress_percent)
st.write(f"Progress: {ensured_count} / {total_questions} questions ensured")

# --- DISPLAY QUESTIONS + ENSURE ---
for category, q_list in questions.items():
    st.subheader(category)
    for idx, question in enumerate(q_list):
        q_key = f"{category}_{idx}"
        response_key = f"{q_key}_response"

        # Default radio selection
        default = st.session_state.responses.get(response_key, "Neutral")
        selected = st.radio(
            question,
            list(scale.keys()),
            key=response_key,
            index=list(scale.keys()).index(default)
        )

        # ENSURE BUTTON
        if q_key not in st.session_state.ensured:
            if st.button(f"Ensure", key=f"ensure_{q_key}"):
                st.session_state.responses[response_key] = selected
                st.session_state.ensured[q_key] = True
                st.experimental_rerun()
        else:
            st.success("Answer ensured.")

# --- SELECT SEX AT THE END ---
st.subheader("Additional Info")
st.selectbox(
    "Please select your sex:",
    options=["Prefer not to say", "Male", "Female", "Other"],
    key="sex"
)

# --- SUBMIT ALL WHEN FINISHED ---
if ensured_count == total_questions:
    if st.button("Submit All Answers"):
        st.session_state.form_submitted = True

# --- EVALUATION ---
if st.session_state.form_submitted:
    total_score = sum(scale[st.session_state.responses[key]] for key in st.session_state.responses)
    avg_score = total_score / total_questions

    st.markdown("### Evaluation Results")
    if avg_score >= 4:
        st.error("You may be experiencing strong imposter syndrome tendencies.")
    elif avg_score >= 3:
        st.warning("You may be experiencing medium imposter syndrome tendencies.")
    else:
        st.success("You may be experiencing low imposter syndrome tendencies.")

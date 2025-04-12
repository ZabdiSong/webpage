import streamlit as st

# -----------------------------
# Session State Initialization
# -----------------------------
if 'answered' not in st.session_state:
    st.session_state.answered = 0
if 'emoji' not in st.session_state:
    st.session_state.emoji = []
if 'question_answered' not in st.session_state:
    st.session_state.question_answered = set()
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False
if 'stages' not in st.session_state:
    st.session_state.stages = set()

# -----------------------------
# Milestones Setup
# -----------------------------
milestones = {
    10: ("🥛", "You are allowed to feel unsure—and still be worthy. Just showing up is enough."),
    30: ("🥜", "You’re not a fraud—you’re just someone growing in a place that never taught you how to feel safe."),
    50: ("🍌", "Impostor syndrome thrives in silence. And you’re breaking that silence, one breath at a time."),
    70: ("🫐", "You’ve worked hard. It’s not luck, and it’s not by accident. You’re allowed to claim it."),
    90: ("🍫", "The voice that says you don’t belong is just fear talking. And you’ve proven it wrong every single day."),
}

# -----------------------------
# Title
# -----------------------------
st.title("Imposter Syndrome Evaluating System")

# -----------------------------
# Questions & Scales
# -----------------------------
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

# -----------------------------
# Display Questions and Track Answers
# -----------------------------
total_score = 0
num_questions = sum(len(qs) for qs in questions.values())

with st.form("evaluation_form"):
    for category, qs in questions.items():
        st.subheader(category)
        for q in qs:
            response = st.radio(q, list(scale.keys()), key=q, index=None)
            # Mark question as answered
            if response is not None:
                if q not in st.session_state.question_answered:
                    st.session_state.question_answered.add(q)

    submitted = st.form_submit_button("Submit")

# -----------------------------
# Progress Calculation
# -----------------------------
st.session_state.answered = len(st.session_state.question_answered)
progress_percent = int((st.session_state.answered / num_questions) * 100)
st.subheader("Progress Bar")
st.progress(progress_percent)

# -----------------------------
# Milestone Rewards
# -----------------------------
for milestone, (emoji, message) in milestones.items():
    if progress_percent >= milestone and milestone not in st.session_state.stages:
        st.session_state.emoji.append(emoji)
        st.session_state.stages.add(milestone)
        st.markdown(f"### {emoji}")
        st.info(message)

# -----------------------------
# Evaluation Logic
# -----------------------------
if submitted:
    if len(st.session_state.question_answered) < num_questions:
        st.warning("Please answer all questions before submitting.")
    else:
        for category, qs in questions.items():
            for q in qs:
                response = st.session_state.get(q)
                if response:
                    total_score += scale[response]

        average = total_score / num_questions
        st.markdown("### Evaluation Results")
        if average >= 4:
            st.error("You may be experiencing strong imposter syndrome tendencies.")
        elif average >= 3:
            st.warning("You may be experiencing medium imposter syndrome tendencies.")
        else:
            st.success("You may be experiencing low imposter syndrome tendencies.")

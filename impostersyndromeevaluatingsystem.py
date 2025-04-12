import streamlit as st

# session state initialize
def reset_session_state():
    st.session_state.answered = 0
    st.session_state.emoji = []
    st.session_state.question_answered = set()
    st.session_state.form_submitted = False
    st.session_state.stages = set()

    # Clear all radio button states
    for category, qs in questions.items():
        for i in range(len(qs)):
            key = f"{category}_{i}"
            if key in st.session_state:
                del st.session_state[key]

if 'answered' not in st.session_state:
    reset_session_state()


# Milestone
milestones = {
    10: ("🥛", "You are allowed to feel unsure—and still be worthy. Just showing up is enough."),
    30: ("🥜", "You’re not a fraud—you’re just someone growing in a place that never taught you how to feel safe."),
    50: ("🍌", "Impostor syndrome thrives in silence. And you’re breaking that silence, one breath at a time."),
    70: ("🫐", "You’ve worked hard. It’s not luck, and it’s not by accident. You’re allowed to claim it."),
    90: ("🍫", "The voice that says you don’t belong is just fear talking. And you’ve proven it wrong every single day."),
}
    
# questions
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

# options
scale = {
    "Strongly Disagree": 1,
    "Disagree": 2,
    "Neutral": 3,
    "Agree": 4,
    "Strongly Agree":5
}

# initialize
st.title("imposter syndrome evaluating system") 
if st.button('Reset'):
    reset_session_state()
    st.experimental_rerun()

# progress
total_questions = sum(len(qs) for qs in questions.values())

answered_count = 0
for category, qs in questions.items():
    for i in range(len(qs)):
        key = f"{category}_{i}"
        if key in st.session_state and st.session_state[key] is not None:
            answered_count += 1

progress_percent = int((answered_count / total_questions) * 100)
st.subheader("Progress")
st.progress(progress_percent)

# milestone
for milestone, (emoji, message) in milestones.items():
    if progress_percent >= milestone and milestone not in st.session_state.stages:
        st.session_state.emoji.append(emoji)
        st.session_state.stages.add(milestone)
        st.markdown(f"### {emoji}")
        st.info(message)

# form
with st.form("imposter_form"):
    total_score = 0
    num_questions = 0

    for category, qs in questions.items():
        st.subheader(category)
        for i, q in enumerate(qs):
            key = f"{category}_{i}"
            response = st.radio(q, list(scale.keys()), key=key, index=None)
            if response:
                total_score += scale[response]
                num_questions += 1

    submitted = st.form_submit_button("Submit")
    if submitted:
        st.session_state.form_submitted = True

# evaluation
if st.session_state.form_submitted and num_questions > 0:
    average = total_score / num_questions
    st.markdown("### Evaluation Results")
    if average >= 4:
        st.error("You may be experiencing strong imposter syndrome tendencies.")
    elif average >= 3:
        st.warning("You may be experiencing medium imposter syndrome tendencies.")
    else:
        st.success("You may be experiencing low imposter syndrome tendencies.")

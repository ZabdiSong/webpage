import streamlit as st

# Define your questions and scale as before...
# (Assume `questions` and `scale` dicts are already declared)

# Initialize session state
if 'response' not in st.session_state:
    st.session_state.responses = {}

# Calculate total number of questions
total_questions = sum(len(qs) for qs in questions.values())
answered_questions = len(st.session_state.responses)

# Progress Calculation
progress = int((answered_questions / total_questions) * 100)
st.markdown("### Fear / Anxiety Progress")
st.progress(progress)

# Emoji Nodes
emoji_nodes = {
    10: "🥛",
    30: "🥜",
    50: "🍌",
    70: "🫐",
    90: "🍫",
    100: "💥"
}
if progress in emoji_nodes:
    st.markdown(f"#### {emoji_nodes[progress]}")

# Questionnaire
for category, qs in questions.items():
    st.subheader(category)
    for q in qs:
        if q not in st.session_state.responses:
            response = st.radio(q, list(scale.keys()), key=q)
            st.session_state.responses[q] = response

# Evaluation
if st.button("Submit"):
    if len(st.session_state.responses) < total_questions:
        st.warning("Please answer all questions before submitting.")
    else:
        scores = [scale[resp] for resp in st.session_state.responses.values()]
        average = sum(scores) / len(scores)

        st.markdown("## Evaluation Results")
        if average >= 4:
            st.error("You may be experiencing **strong** imposter syndrome tendencies.")
        elif average >= 3:
            st.warning("You may be experiencing **moderate** imposter syndrome tendencies.")
        else:
            st.success("You may be experiencing **low** imposter syndrome tendencies.")
        st.balloons()  # Celebration at 100%

import streamlit as st

st.title("Own it log - your effort tracker")

# input
with st.form("init_form", clear_on_submit=False):
    goal = st.text_input("Goal", placeholder="e.g., Submit research paper")
    mindset = st.text_area("Mindset", placeholder="What are you feeling before starting?")
    challenge = st.text_area("Challenges", placeholder="What obstacles do you foresee?")
    start = st.form_submit_button("Create Task")

# initialization
if start:
    st.session_state["effort_log"] = []
    st.session_state["goal"] = goal
    st.session_state["mindset"] = mindset
    st.session_state["challenge"] = challenge
    st.success("Task initialized!")

# timeline import
if "effort_log" in st.session_state:
    st.markdown("### Record Progress")

    with st.form("log_form"):
        note = st.text_area("What did you do or feel?")
        log_button = st.form_submit_button("Add to Timeline")
    
    if log_button and note:
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.session_state["effort_log"].append((timestamp, note))
        st.success("Log added!")

# timeline presentation
if st.button("Finish Task and Show Timeline"):
    st.markdown("## Final Timeline")

    st.markdown(f"**Goal:** {st.session_state['goal']}")
    st.markdown(f"**Mindset:** {st.session_state['mindset']}")
    st.markdown(f"**Challenges:** {st.session_state['challenge']}")
    
    st.markdown("### Task Log Timeline")
    for ts, log in st.session_state["effort_log"]:
        st.markdown(f"- **{ts}**: {log}")

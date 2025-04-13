import streamlit as st
import re

# wordlist
positive_words = ["grateful", "happy", "calm", "hope", "safe", "love", "joy", "peace", "excited"]
negative_words = ["anxious", "afraid", "sad", "angry", "nervous", "lonely", "panic", "overwhelmed"]

# initialize
st.markdown("### Mindfulness Journal")
st.markdown("> You are currently experiencing an uncomfortable emotion. We are here with you to witness it together. Write down the emotions and thoughts that you are currently feeling.")

# user input
text = st.text_area("Your thoughts", height=200)

def highlight_emotions(text):
    word_list = re.findall(r'\b\w+\b', text.lower())
    highlighted_text = text

    pos_count = 0
    neg_count = 0

    for word in set(word_list):
        if word in positive_words:
            highlighted_text = re.sub(rf'\b({word})\b', r'<span style="color:orange; font-weight:bold;">\1</span>', highlighted_text, flags=re.IGNORECASE)
            pos_count += word_list.count(word)
        elif word in negative_words:
            highlighted_text = re.sub(rf'\b({word})\b', r'<span style="color:gray;">\1</span>', highlighted_text, flags=re.IGNORECASE)
            neg_count += word_list.count(word)

    return highlighted_text, pos_count, neg_count

if text:
    styled_text, pos_total, neg_total = highlight_emotions(text)
    st.markdown("### Emotional Highlighting", unsafe_allow_html=True)
    st.markdown(styled_text, unsafe_allow_html=True)

    # analysis
    st.markdown("---")
    st.markdown("### Word Analysis")
    st.markdown(f"- Positive words: **{pos_total}**")
    st.markdown(f"- Negative words: **{neg_total}**")
import streamlit as st

# Define login function
def login(username, password):
    # Validation logic
    if username == "123456" and password == "123456":
        return "https://www.douyin.com"
    else:
        return "登录失败,请重试。"

# Create a title
st.title("登录界面")

# Username input
username = st.text_input("用户名:")

# Password input
password = st.text_input("密码:", type='password')

# Login button
if st.button("登录"):
    result = login(username, password)
    st.write(result)

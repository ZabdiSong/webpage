import streamlit as st

# Clear page
st.empty()

# Set title
st.title("江苏国邦石油化工有限公司油库IC卡管理系统")

# Set Columns
answer = st.selectbox("分区选择", ("基础设置", "销售管理", "报表"))
st.empty()

# Column 1
if answer == "基础设置":
    st.empty()
    st.title("基础设置")
    column1 = st.selectbox("设置选择", ("员工设置", "油品设置"))
    
    if column1 == "员工设置":
        st.empty()
        

  
    
    

import streamlit as st


# Clear page
st.empty()

# Set title
st.title("江苏国邦石油化工有限公司油库IC卡管理系统")

# Set Columns
answer = st.selectbox("分区选择", ("基础设置", "销售管理", "报表"))

# Column 1
if answer == "基础设置":
    st.empty()
    st.title("基础设置")
    column1 = st.selectbox("设置选择", ("员工设置", "油品设置"))

    # Set 1
    if column1 == "员工设置":
        st.empty()
        st.title("员工设置")
        set1 = st.selectbox("设置选择", ("新增", "修改", "删除"))

    
    # Adding 
        if set1 == "新增":
            st.empty()
            operate1 = int(input("输入项目"))
            issue1 = st.selectbox("设置选择", ("确定", "取消"))
         
            if issue1 == "确定":
                print(operate1)
            
            elif issue1 == "取消":
                print(" ")


    
    # Set 2   
    elif column1 == "油品设置":
        st.empty()
        st.title("油品设置")
        set2 = st.selectbox("设置选择", ("新增", "修改", "启用", "禁用"))



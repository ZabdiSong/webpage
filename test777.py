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
    column1 = st.selectbox("员工设置", "油品设置")

    # Set 1
    if column1 == "员工设置":
        st.empty()
        st.title("员工设置")
        set1 = st.selectbox("新增", "修改", "删除")
    
    # Set 2
    elif column1 == "油品设置":
        st.empty()
        st.title("油品设置")
        set2 = st.selectbox("新增", "修改", "启用", "禁用")


# Column 2
if answer == "销售管理":
    st.empty()
    st.title("销售管理")
    column2 = st.selectbox("销售单制作（主管）", "分提单制作")

    # Set 3
    if column2 == "销售单制作（主管）":
        st.empty()
        st.title("销售单制作（主管）")
        set3 = st.selectbox("确定", "取消")

    # Set 4
    elif column2 == "分提单制作":
        st.empty()
        st.title("分提单制作")
        set4 = st.selectbox("查询", "分提", "作废")

# Column 3
if answer == "报表":
    st.empty()
    st.title("报表")
    column3 = st.selectbox("销售明细", "客存销售实时统计")

    # Set 5
    if column3 == "销售明细":
        st.empty()
        st.title("销售明细")
        set5 = st.button("查询")

    # Set 6
    elif column3 == "客存销售实时统计":
        st.empty()
        st.title("客存销售实时统计")
        set6 = st.button("查询")

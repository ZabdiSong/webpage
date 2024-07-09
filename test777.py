import streamlit as st
import tkinter as tk
from tkinter import ttk
import webbrowser



#定义登陆
def login():
    username = username_entry.get()
    password = password_entry.get()
    number = number_entry.get()
    name = name_entry.get()
    branch = branch_entry.get()
    phone = phone_entry.get()
    remarks = remarks_entry.get()
    #验证逻辑
    if username == "123456" and password == "123456":
        webbrowser.open("https://www.douyin.com")
    else:
        print("登录失败,请重试。")
#创建窗口
root = tk.Tk()
root.title("登录界面")
root.geometry("600x400")
#员工编号输入
number_label = ttk.Label(root, text="员工编号:")
number_label.grid(row=0, column=0, padx=10, pady=10)
#显示员工编号
number_entry = ttk.Entry(root)
number_entry.grid(row=0, column=1, padx=10, pady=10)
#员工名称输入
username_label = ttk.Label(root, text="员工姓名:")
username_label.grid(row=1, column=0, padx=10, pady=10)
#显示员工名称
username_entry = ttk.Entry(root)
username_entry.grid(row=1, column=1, padx=10, pady=10)
#密码输入
password_label = ttk.Label(root, text="密码:")
password_label.grid(row=2, column=0, padx=10, pady=10)
#隐藏密码
password_entry = ttk.Entry(root, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=10)
#登陆输入
login_button = ttk.Button(root, text="登录", command=login)
login_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)
#员工角色输入
name_label = ttk.Label(root, text="角色名称:")
name_label.grid(row=3, column=0, padx=10, pady=10)
#显示员工角色
name_entry = ttk.Entry(root)
#部门名称输入
branch_label = ttk.Label(root, text="员工编号:")
branch_label.grid(row=4, column=0, padx=10, pady=10)
#显示部门名称
branch_entry = ttk.Entry(root)
#电话输入
phone_label = ttk.Label(root, text="手机号码:")
phone_label.grid(row=5, column=0, padx=10, pady=10)
#显示电话
phone_entry = ttk.Entry(root)
phone_entry.grid(row=5, column=1, padx=10, pady=10)
#备注输入
remarks_label = ttk.Label(root, text="备注:")
remarks_label.grid(row=6, column=0, padx=10, pady=10)
#显示备注
remarks_entry = ttk.Entry(root)
remarks_entry.grid(row=6, column=1, padx=10, pady=10)
#列表展开
def show_options(event):
    options_listbox.grid(row=3, column=1, padx=10, pady=10)
    #将selected_label隐藏
    selected_label.grid_remove()
def show_options2(event2):
    options_listbox2.grid(row=4, column=1, padx=10, pady=10)
    #将selected_label2隐藏
    selected_label2.grid_remove()
#列表关闭
def hide_options(event):
    options_listbox.grid_forget()
def hide_options2(event2):
    options_listbox2.grid_forget()
#列表选择
def select_option(event):
    selected_option = options_listbox.get(options_listbox.curselection())
    selected_label.config(text=f"{selected_option}")
    #将selected_label显示
    selected_label.grid()
    hide_options(event)
def select_option2(event2):
    selected_option2 = options_listbox2.get(options_listbox2.curselection())
    selected_label2.config(text=f"{selected_option2}")
    #将selected_label2显示
    selected_label2.grid()
    hide_options2(event2)
# 主输入框
input_entry = ttk.Entry(root)
input_entry.grid(row=3, column=1, padx=10, pady=10)
input_entry.bind("<Button-1>", show_options)
input_entry.bind("<FocusOut>", hide_options)

input_entry2 = ttk.Entry(root)
input_entry2.grid(row=4, column=1, padx=10, pady=10)
input_entry2.bind("<Button-1>", show_options2)
input_entry2.bind("<FocusOut>", hide_options2)

# 选项列表
options = ["管理员", "报表员", "快递员"]
options_listbox = tk.Listbox(root,height=len(options))
for option in options:
    options_listbox.insert(tk.END, option)
options_listbox.grid_forget()  
options2 = ["外交部门", "商业部门", "行政部门"]
options_listbox2 = tk.Listbox(root,height=len(options2))
for option2 in options2:
    options_listbox2.insert(tk.END, option2)
options_listbox2.grid_forget()  

# 初始隐藏列表
options_listbox.bind("<<ListboxSelect>>", select_option)
options_listbox2.bind("<<ListboxSelect>>", select_option2)

# 已选择的选项
selected_label = ttk.Label(root, text="请选择角色")
selected_label.grid(row=3, column=1, padx=10, pady=10)
selected_label.bind("<Button-1>", show_options)
selected_label.bind("<FocusOut>", hide_options)
selected_label2 = ttk.Label(root, text="请选择部门")
selected_label2.grid(row=4, column=1, padx=10, pady=10)
selected_label2.bind("<Button-1>", show_options2)
selected_label2.bind("<FocusOut>", hide_options2)



root.mainloop()










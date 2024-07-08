import streamlit as st
import tkinter as tk
from tkinter import ttk
import webbrowser



#定义登陆
def login():
    username = username_entry.get()
    password = password_entry.get()
    #验证逻辑
    if username == "123456" and password == "123456":
        webbrowser.open("https://www.douyin.com")
    else:
        print("登录失败,请重试。")
#创建窗口
root = tk.Tk()
root.title("登录界面")
root.geometry("600x400")
#用户名输入
username_label = ttk.Label(root, text="用户名:")
username_label.grid(row=0, column=0, padx=10, pady=10)
#显示用户名
username_entry = ttk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=10)
#密码输入
password_label = ttk.Label(root, text="密码:")
password_label.grid(row=1, column=0, padx=10, pady=10)
#隐藏密码
password_entry = ttk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)
#登陆输入
login_button = ttk.Button(root, text="登录", command=login)
login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)




root.mainloop()










from tkinter import *
wid = Tk()
wid.title("用户登录")
wid.geometry("300x200")
# 事件的触发及逻辑
def identify():
    global lab_3
    username = txt_1.get()
    password = txt_2.get()
    if username == "aaa" and password == "aaa":
        lab_3.configure(text="登录成功")
    elif username != "aaa":
        lab_3.configure(text="用户名不存在")
        txt_v_1.set("")
        txt_v_2.set("")
    elif password != "aaa":
        lab_3.config(text="密码不正确")
        txt_v_2.set("")
# 定义所需的元素
lab_1 = Label(wid, text="用户名:")
lab_2 = Label(wid, text="密码:")
lab_3 = Label(wid, font=("黑体", 12))
txt_v_1 = StringVar()
txt_v_2 = StringVar()
txt_1 = Entry(wid, textvariable=txt_v_1)
txt_2 = Entry(wid, textvariable=txt_v_2)
but_1 = Button(wid, text="登录", command=identify)
# 排版元素的布局
lab_1.grid(column=0, row=0)
lab_2.grid(column=0, row=1, ipady=8)
lab_3.place(x=100, y=120)
txt_1.grid(column=2, row=0, ipadx=250, ipady=8)
txt_2.grid(column=2, row=1, ipadx=250, ipady=8)
but_1.place(x=120, y=80)
wid.mainloop()

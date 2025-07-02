from tkinter import *
import random
# 创建窗口
wid = Tk()
wid.title("水果统计")
wid.geometry("300x200")
# 事件触发与处理
def get_re():
    re_str = count_one_fruit(ent_1.get())
    txt_1.insert(END, re_str)


def count_one_fruit(fruit_name):
    # 统计水果数量
    list_target = ['香蕉', '草莓', '苹果', '梨子', '西瓜', '芒果', '葡萄']
    re_list = []
    num = 0
    while num < 100:
        re_list.append(random.choice(list_target))
        num += 1
    return f"随机100次共得到了{re_list.count(fruit_name)}个{fruit_name}\n"
# 设定元素
lab_1 = Label(wid, text="请在输入框中输入任意的水果名")
ent_1 = Entry(wid)
btn_1 = Button(wid, text="提交", command=get_re)
txt_1 = Text(wid)
# 元素布局
lab_1.pack()
ent_1.pack()
btn_1.pack()
txt_1.pack()
wid.mainloop()

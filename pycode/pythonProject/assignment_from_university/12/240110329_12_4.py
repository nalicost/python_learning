from tkinter import *
from tkinter.simpledialog import *
num_cost = 0
wid = Tk()
wid.title("自助点餐")
wid.geometry("300x300")


# 事件触发与处理
def get_check_out(on_sale_rate=1.0):
    global num_cost
    dict_food, re_list, re_num = {1: (12, "汉堡包"), 2: (7, '蛋挞'), 3: (10, "猪肉卷"), 4: (5, "饮料")}, [], 0
    for item_1 in (cbv_1, cbv_2, cbv_3, cbv_4):
        if item_1.get():
            info_item = dict_food[item_1.get()]
            re_num += info_item[0]
            re_list.append(info_item[1])
    re_str_food = '和'.join(re_list)
    num_cost = re_num * on_sale_rate
    lab_2.configure(text=f"您点了{re_str_food}，一共{num_cost}元")


def identify_vip():
    vip_code = askstring("会员付款界面", "请输入会员码")
    if vip_code == "abcdefg":
        get_check_out(0.8)
    else:
        get_check_out()


def pay_mon():
    global num_cost
    num = int(ent_1.get())
    if num < num_cost:
        lab_3.configure(text="金额不足")
    elif num == num_cost:
        lab_3.configure(text=f"收费{num}元")
    else:
        lab_3.configure(text=f"收费{num_cost}元, 找零{num - num_cost}元")


# 定义元素
lab_1 = Label(wid, text="您好，请问需要什么")
cbv_1, cbv_2, cbv_3, cbv_4 = IntVar(), IntVar(), IntVar(), IntVar()
cb_1 = Checkbutton(wid, text="汉堡包：12元", variable=cbv_1, onvalue=1, offvalue=0)
cb_2 = Checkbutton(wid, text="蛋挞：7元", variable=cbv_2, onvalue=2, offvalue=0)
cb_3 = Checkbutton(wid, text="猪肉卷：10元", variable=cbv_3, onvalue=3, offvalue=0)
cb_4 = Checkbutton(wid, text="饮料：5元", variable=cbv_4, onvalue=4, offvalue=0)
btn_1 = Button(wid, text="OK")
lab_2 = Label(wid)
ent_1 = Entry(wid)
btn_2 = Button(wid, text="付款", command=pay_mon)
lab_3 = Label(wid)
# 元素布局
for item in (lab_1, cb_1, cb_2, cb_3, cb_4, btn_1, lab_2, ent_1, btn_2, lab_3):
    item.pack()
btn_1.bind("<1>", lambda x: get_check_out())
btn_1.bind("<3>", lambda x: identify_vip())
btn_1.focus_set()
wid.mainloop()

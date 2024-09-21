meua= {'北京': {'海淀': {'五道口': {'soha': {}, '网易': {}, 'google': {}}, '中关村': {'爱奇艺': {}, '汽车之家': {}, 'youku': {}}, '上地': {'百度': {}}}, '昌平': {'沙河': {'路飞学城': {}, '北航': {}}}, '天通苑': {}, '回龙观': {}, '朝阳': {}, '东城': {}}, '上海': {'闵行': {'人民广场': {'炸鸡店': {}}}, '闸北': {'火车站': {'携程': {}}}, '浦东': {}}, '山东': {}}
meua_process = meua
option = {0: meua, 1: 1, 2: 2, 3: 3,4:4} #分别存入0，1，2，3，4级菜单选取的内容
i = 0
print('请输入菜单中的内容进入下一层，按b返回上一层，按q退出菜单')
while i <= len(option)-1:  #循环继续的条件
    print(f'{i+1}级目录') #显示层数
    for output in option[i].keys(): #将该层中所有key，即目录取出，并打印
        print(output)
    print() #转行
    choice = input('您选择的菜单：').strip()
    if choice == 'b' and i != 0: #返回上一层，且保证不是在初始层
        i -= 1 #将层数减一
        meua_process = option[i] #将上一次目录选取吊出，并重新为meua_process赋值，以供等会目录打印
    elif choice == 'q': #退出条件
        i = len(option)
    elif choice not in meua_process or choice == 'b' and i == 0: #对非法输入进行提示
        print('请输入目录中的内容或返回上一目录')
    elif len(meua_process) != 0: #判断是否已经到最后一层了，是那么无论做什么层数都不会增加，否则执行下方代码
        meua_process=meua_process[choice] #将选取的目录对应的下一级目录重新复值给meua_process，以供等会将目录打印
        option[i + 1] = meua_process #记录下此次选取的目录
        i += 1 #层数加一
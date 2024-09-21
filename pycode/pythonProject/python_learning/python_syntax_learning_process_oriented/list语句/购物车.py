i=1
money_remain=0
money_all=0
user_command=''
good_list=[[1,' iphone',7000],[2,' ipad',9000],[3,' pen',15],[4,' book',20],[5,' water',2],[6,' booklet',4000],[7,' reminder',200],[8,' rock',5],[9,' calculator',200],[10,' battery',20],[11,' tv',3000],[12,' bike',700],[13,' watch',1500],[14,' coco cola',5],[15,' steak',70],[16,' blouse',300],[17,' football shoes',400],[18,' hot dog',7],[19,' ice cream',1],[20,' sun glasses',150]]
shopping_list=[[0,'iphone',7000],[0,'ipad',9000],[0,'pen',15],[0,'book',20],[0,'water',2],[0,'booklet',4000],[0,'reminder',200],[0,'rock',5],[0,'calculator',200],[0,'battery',20],[0,'tv',3000],[0,'bike',700],[0,'watch',1500],[0,'coco cola',5],[0,'steak',70],[0,'blouse',300],[0,'football shoes',400],[0,'hot dog',7],[0,'ice cream',1],[0,'sun glasses',150]]
list_all=[['good list',good_list,0],['shopping list',shopping_list,1]]#替换下方重复代码的关键词，保证代码简洁
for k in list_all:
    print(k[0].center(104,'-'))#生成打印出来的list的标题
    for item in k[1]:#取出列表
        if 0 not in item:#确保取出的第二个购买列表项是有购买的同时不影响第一个list内容的打印
            space_len_1=100-len(str(item[0]))-len(str(item[1]))-len(str(item[2]))#用来填充字符与字符间的空隙，保证总字符长度恒定
            print(item[0],item[1],' '*space_len_1,item[2])
    if k[2]==1:#确保第二次打印时候打印时候能打印余额和消费额，同时保证第一次打印list不受影响
        space_len_2=100-len(str(money_all-money_remain))-10#用来填充字符与字符间的空隙，保证总字符长度恒定
        space_len_3=100-len(str(money_remain))-8#用来填充字符与字符间的空隙，保证总字符长度恒定
        print('你的总开销为：',' '*space_len_2,money_all-money_remain)
        print('你的余额为:',' '*space_len_3,money_remain)
    print('end'.center(104,'-'))#生成打印出来的list的结尾
    if k[2]==0:#确保仅在第一次时候打印要求
        print('''
        查看目前购买数量请在功能选择处输入0。
        再次查看商品列表请在功能选择处输入1。
        查看余额请在功能选择处输入2。
        在功能处不输入或输入其他默认进入选购模式。
        请自行输入你想购买物品的编码以及正的数量。
        想要退货请输入货品编码以及负的数量。
        退出时请输入物品编码0以及数量0或其他数字
        ''')
    while i != 0:#用来保证可以连续的充值
        money=input('你的经费是：').strip()
        if money.isdigit():#以下语句用来记录余额和总金额
            money_remain += int(money)
            money_all += int(money)
            while i != 0:#用来保证可以连续的选择服务并运行服务
                service=input('你选择的要使用的功能是：')
                if service == '0' or service == '1':#实现0，1服务合并打印，同上放打印内容
                    print(k[0].center(104, '-'))
                    for item_0 in list_all[int(service)][1]:
                        if 0 not in item_0:
                            space_len_1 = 100 - len(str(item_0[0])) - len(str(item_0[1])) - len(str(item_0[2]))
                            print(item_0[0], item_0[1], ' ' * space_len_1, item_0[2])
                    print('end'.center(104, '-'))
                elif service == '2':print('你的余额为：', money_remain)#实现打印余额
                else:
                    buy=input('你选择的货物编码是：').strip()
                    nul=input('你想要的数量是：').strip()
                    nul=' '+nul#防止由于nul不输入内容，导致报错
                    if buy.isdigit() and 0<= int(buy) <= good_list[-1][0] and nul[-1].isdigit():#最后一个判断可以保证当输入数字时不会因为前面加入空格而恒输出False
                        buy=int(buy)
                        nul=int(nul)
                        if buy == 0:i = buy#保证输出0时程序退出
                        elif money_remain >= good_list[buy-1][2]*nul and -nul <= shopping_list[buy-1][0]:#前者保证余额大于所购买物体的金额，后者保证退货时不会超过已购买的数量
                            money_remain -= good_list[buy-1][2]*nul#更改余额
                            shopping_list[buy-1][0] += nul#更改购买数量
                            print('你的余额为：', money_remain)
                        else:
                            user_command=input('余额不足，是否增加预算，是写yes，否写no：').strip()
                            if user_command == 'yes':break#若是要充值则结束功能循环回到外层充值循环
                            else:print('已取消本次订单。')#若是不合法则回到功能循环
                    else:print("请输入正确的值。")#若是不合法则回到功能循环
        else:
            print("请输入正确的值。")#若是不合法则回到充值循环
print('谢谢惠顾。')#结束语
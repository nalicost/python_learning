import random
with open(r'C:\Users\zhang\Desktop\东华大学\newscore.txt', 'r', encoding='utf8') as f_old:
    province_list = ['河北省', '山西省', '辽宁省', '吉林省', '黑龙江省', '江苏省', '浙江省', '安徽省', '福建省', '江西省', '山东省',
                     '河南省', '湖北省', '湖南省', '广东省', '海南省', '四川省', '贵州省', '云南省', '陕西省', '甘肃省', '青海省',
                     '台湾省', '内蒙古自治区', '广西壮族自治区', '西藏自治区', '宁夏回族自治区', '新疆维吾尔自治区', '北京市', '天津市',
                     '上海市', '重庆市']
    with open(r'studentinfo.txt', 'w', encoding='utf8') as f_new:
        for item in f_old:
            f_new.write(item.strip() + ',' + random.choice(province_list) + '\n')

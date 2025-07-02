# file: website1/views.py
from django.http import HttpResponse
from django.shortcuts import render


def index_view(request):
    html_l = f"<h1>这是主页</h1>"
    return HttpResponse(html_l)


def page1_view(request):
    html_l = "<h1>这是第一个页面</h1>"
    return HttpResponse(html_l)


def page2_view(request):
    html_l = "<h1>这是第二个页面</h1>"
    return HttpResponse(html_l)


def pagen_view(request, n):
    html_l = f"<h1>这是第{n}个页面</h1>"
    return HttpResponse(html_l)


def cal_view(request, *args):
    if args[1] == "add":
        num = int(args[0]) + int(args[2])
    elif args[1] == "mul":
        num = int(args[0]) * int(args[2])
    elif args[1] == "sub":
        num = int(args[0]) - int(args[2])
    else:
        return
    html_l = f"<h1>答案是：{num}</h1>"
    return HttpResponse(html_l)


def birth_view(request, **kwargs):
    html_l = f"生日为：{kwargs['year']}年{kwargs['month']}月{kwargs['day']}日"
    return HttpResponse(html_l)


def cal_sum_view(request):
    data_index, re_list = ["start", "stop", "step"], []
    if request.method == "GET":
        for i in range(len(data_index)):
            try:
                num = request.GET.get(data_index[i], 'none')
                num = num if i != 2 or num != 'none' else '1'
                re_list.append(int(num))
            except Exception:
                return HttpResponse(f"<h1 style='color:red;'>请输入正确的值</h1>")
    start, stop, step = re_list
    re_num = (((stop - start) // step + 1) * start +
              ((stop - start) // step + 1) * ((stop - start) // step) / 2 * step)
    return HttpResponse(f"<h1 style='color:blue;'>答案是：{re_num}</h1>")


def calculater_view(request):
    try:
        if request.method == "GET":
            return render(request, "calculator.html")
        elif request.method == "POST":
            dic_cal = dict(request.POST)
            cal_type, val_f, val_e = dic_cal["type"][0], int(dic_cal["val_1"][0]), int(dic_cal["val_2"][0])
            if cal_type == "+":
                res = val_f + val_e
                sel_1 = "selected"
            elif cal_type == "-":
                res = val_f - val_e
                sel_2 = "selected"
            elif cal_type == "*":
                res = val_f * val_e
                sel_3 = "selected"
            else:
                res = round(val_f / val_e, 2)
                sel_4 = "selected"
            return render(request, "calculator.html", locals())
    except Exception:
        return HttpResponse(f"<h1 style='color:red;'>请输入正确的值</h1>")


class TaxProModel:
    def __init__(self, proj, sel_mon, ent_mon, loc='01'):
        self.proj = proj
        self.self_mon = sel_mon
        self.ent_mon = ent_mon
        self.loc = loc


def cal_tax_view(request):
    if request.method == 'GET':
        return render(request, "tax_cal.html")
    elif request.method == 'POST':
        try:
            re, pos_dic, pro_conf_li, re_list = ('op',
                                                 dict(request.POST),
                                                 [
                                                     ['养老保险', (0.08, 0), (0.19, 0)],
                                                     ['失业', (0.002, 0), (0.008, 0)],
                                                     ['失业', (0, 0), (0.008, 0), '1'],
                                                     ['工伤保险', (0, 0), (0.005, 0)],
                                                     ['生育保险', (0, 0), (0.008, 0)],
                                                     ['医疗保险', (0.02, 3), (0.1, 0)],
                                                     ['公积金', (0.12, 0), (0.12, 0)],
                                                     ['个人纳税总和', (0.222, 3), (0, 0)],
                                                     ['公司纳税总和', (0.439, 0), (0, 0)],
                                                     ['纳入国家全额总和', (0.661, 3), (0, 0)]
                                                 ],
                                                 []
                                                 )
            base, loc = int(pos_dic['baseNum'][0]), str((pos_dic['type'][0]))
            pro_conf_li = [TaxProModel(*item) for item in pro_conf_li]
            for ite in range(len(pro_conf_li)):
                obj = pro_conf_li[ite]
                if loc in obj.loc:
                    re_ite = TaxProModel(obj.proj,
                                         obj.self_mon[0] * base + obj.self_mon[1],
                                         obj.ent_mon[0] * base + obj.ent_mon[1])
                    re_list.append([re_ite, len(re_list) % 2])
            return render(request, "tax_cal.html", locals())
        except Exception:
            re_list = []
            return render(request, "tax_cal.html", locals())



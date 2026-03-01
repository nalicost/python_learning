from urllib import request
import re
import time
import random
import csv

re_lis = []

for item in range(10):

    # headers可以参照正常浏览器的请求头，注意一定要删除其中含有gzip的请求头，这会使获得的内容被压缩，无法解码
    req = request.Request(url=f'https://www.maoyan.com/board/4?index=2&offset={item * 10}',
                          headers={
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control":"no-cache",
        "Connection":"keep-alive",
        "Cookie":"__mta=146119179.1771785010923.1771855350064.1771855902890.16; uuid_n_v=v1; uuid=853FDDC0101C11F1A5C849EB466CB8DA906C493754BD4DB4BD8C237D43526AFB; _lxsdk_cuid=19c869dbe7fc8-0b285d0ea5ea77-4c657b58-384000-19c869dbe7fc8; _lxsdk=853FDDC0101C11F1A5C849EB466CB8DA906C493754BD4DB4BD8C237D43526AFB; _ga=GA1.1.1738803399.1771785011; _lx_utm=utm_source%3Dbing%26utm_medium%3Dorganic; __mta=146119179.1771785010923.1771852015447.1771852031692.5; _csrf=9bb090f384322f54b1ed23a8d835aff8ebe41e5792a55f86e21657a04180fcd8; _ga_WN80P4PSY7=GS2.1.s1771855319$o3$g1$t1771855902$j60$l0$h0; Hm_lvt_e0bacf12e04a7bd88ddbd9c74ef2b533=1771785011,1771851996,1771855903; Hm_lpvt_e0bacf12e04a7bd88ddbd9c74ef2b533=1771855903; HMACCOUNT=B4051D08117F9661; _lxsdk_s=19c8ace8f2e-259-ce0-688%7C%7C7",
        "Host":"www.maoyan.com",
        "Pragma":"no-cache",
        "Sec-Fetch-Dest":"document",
        "Sec-Fetch-Mode":"navigate",
        "Sec-Fetch-Site":"same-origin",
        "Sec-Fetch-User":"?1",
        "Upgrade-Insecure-Requests":"1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0",
        "sec-ch-ua":"'Not:A-Brand';v='99', 'Microsoft Edge';v='145', 'Chromium';v='145'",
        "sec-ch-ua-mobile":"?0",
        "sec-ch-ua-platform":"'Windows'"
    })
    response = request.urlopen(req)
    html = response.read().decode("utf8")


    regex = re.compile(r'<div class="movie-item-info">.*?title="(.*?)"', re.S)
    lis = regex.findall(html)
    re_lis.append(lis)
    time.sleep(random.randint(1, 3))

with open("maoyan.csv", "w", encoding="utf-8", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(re_lis)
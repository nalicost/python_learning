from urllib import request, parse

original_str = "妹妹"


req = request.Request(url=f'https://pop5.4i5x.com/search.php?step=2&f_fid=all&keyword={parse.quote(original_str)}&method=AND&f_fid=all&old=cs&page=1', headers={
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "cookie": "safe18_pass=pop5.4i5x.com%7C1771788561%7Cb1925eeef9754601a2d32704e8f17db2948055bb852d7bbf463c8e786b535b9f; zh_choose=n; a22e7_threadlog=%2C3%2C43%2C; a22e7_readlog=%2C24709397%2C24710617%2C24713438%2C; a22e7_lastpos=other; a22e7_cknum=Aw8CUAoCAlhXAWs5AldTUAUDVA8HUFECAlNXXwYGWlAJVV4AAAgGAFRRU1I%3D; a22e7_winduser=BwwHVwINAmhTD1YGAlsFU1YBC1oEUAUGUlFUXQMEUVBWAV8DAAwEBzsEVFJSAVIAWlJU; a22e7_ck_info=%2F%09; a22e7_ol_offset=32592; a22e7_lastvisit=19%091771865999%09%2Fsearch.php%3Fstep%3D2%26f_fid%3Dall%26keyword%3D%25E5%25A7%2590%25E5%25A7%2590%26method%3DAND%26f_fid%3Dall%26old%3Dcs%26page%3D4",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "sec-ch-ua": '"Not:A-Brand";v="99", "Microsoft Edge";v="145", "Chromium";v="145"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0",
})

response = request.urlopen(req)
html = response.read().decode('utf-8')

with open("result.html", "w", encoding="utf-8") as f:

    f.write(html)

print("完成")
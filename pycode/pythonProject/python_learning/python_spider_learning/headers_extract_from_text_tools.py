import json
import re

re_dic = {}
lis = []

print("请输入请求头")

while True:

    st = input()

    if st.strip() == "exit":

        break

    st = re.sub('"', "'", st)
    lis.append(st)

for li in lis:

    li = li.strip()
    item = li.split(": ")
    re_dic[item[0]] = item[1]

with open("temporary.txt", "w", encoding="utf-8") as f:

    f.write(json.dumps(re_dic, ensure_ascii=False, indent=4, separators=(", ", ": ")))

print(f"\n\r\n\r{"=" * 20}\n\r解析完成")
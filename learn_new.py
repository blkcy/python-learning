# 1. 让用户输入，存进变量
username = input("请输入你的名字：")

# 2. 注意：input 接收到的永远是“字符串”
# 如果要算数学，必须用 float() 转成小数，或者 int() 转成整数
age = int(input("请输入你的年龄："))

# 3. f-string 格式化输出（把变量塞进句子里）
print(f"你好，{username}。你今年 {age} 岁，明年你就 {age + 1} 岁了。")
# 1. 创建一个空字典（大括号）
hero = {}

# 2. 往字典里存数据（键: 值）
hero["name"] = "子白"
hero["hp"] = 100

# 3. 修改字典里的数据（比如扣血）
hero["hp"] -= 20  # 现在 hp 变成了 80

# 4. 判断某个键在不在字典里（用 in）
if "hp" in hero:
    print(f"子白当前的HP是：{hero['hp']}")

# 5. 遍历字典（拿出所有的键和值）
# 这里的 k 代表键(key)，v 代表值(value)
for k, v in hero.items():
    print(f"属性：{k}，数值：{v}")
import json

# 准备一个要保存的数据（列表里装字典）
save_data = [{"name": "子白", "level": 1}, {"name": "伊莱", "level": 99}]

# 1. 写入文件（"w"模式，会把数据变字符串存进硬盘）
# ensure_ascii=False 是为了防止中文变成乱码
with open("save_test.txt", "w", encoding="utf-8") as f:
    json.dump(save_data, f, ensure_ascii=False)

# 2. 读取文件（"r"模式，把硬盘里的字符串变回Python的数据）
with open("save_test.txt", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
    print("读取到的数据：", loaded_data)
import requests
from bs4 import BeautifulSoup

# 1. 伪装成浏览器（Headers 其实就是个字典）
headers = {"User-Agent": "Mozilla/5.0"}

# 2. 发送 GET 请求，把网页源码抓下来
response = requests.get("http://quotes.toscrape.com/", headers=headers)

# 3. 判断状态码是不是 200（200代表成功）
if response.status_code == 200:
    # 4. 把源码丢给 BeautifulSoup 解析
    soup = BeautifulSoup(response.text, "html.parser")

    # 5. 找所有的名言卡片（class_ 注意有个下划线）
    cards = soup.find_all("div", class_="quote")

    # 6. 提取第一张卡片的文字
    first_text = cards[0].find("span", class_="text").text
    print("抓到的第一条名言是：", first_text)
else:
    print("抓取失败，状态码：", response.status_code)
import requests
from bs4 import BeautifulSoup

# 目标网址（新手练习爬虫的网站）
url = "http://quotes.toscrape.com/"

# 伪装成浏览器
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

print("正在潜入目标网站...")
response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("潜入成功！开始解析数据...\n")

    # 解析网页
    soup = BeautifulSoup(response.text, "html.parser")

    # 找到所有名言卡片
    quotes = soup.find_all("div", class_="quote")

    for q in quotes:
        text = q.find("span", class_="text").text
        author = q.find("small", class_="author").text
        print(f"【名言】{text}")
        print(f"【作者】{author}")
        print("-" * 30)
else:
    print("潜入失败，状态码：", response.status_code)
import requests
from bs4 import BeautifulSoup
import json

url = "http://quotes.toscrape.com/"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")

    # 1. 准备一个大箱子，把抓到的名言装进去
    all_quotes = []

    for q in quotes:
        text = q.find("span", class_="text").text
        author = q.find("small", class_="author").text

        # 把名言和作者打包成字典，放进列表
        all_quotes.append({"名言": text, "作者": author})

    # 2. 用你学过的文件读写，存到 D 盘
    with open("quotes.txt", "w", encoding="utf-8") as f:
        json.dump(all_quotes, f, ensure_ascii=False, indent=4)  # indent=4 会让文件排版很好看

    print(f"抓取完成！成功将 {len(all_quotes)} 条名言存入 quotes.txt 文件！")
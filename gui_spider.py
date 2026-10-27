import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup


def get_quotes():
    url = "http://quotes.toscrape.com/"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            quotes = soup.find_all("div", class_="quote")

            # 清空文本框里的旧内容
            text_area.delete(1.0, tk.END)

            # 把抓到的内容写进文本框
            for q in quotes:
                text = q.find("span", class_="text").text
                author = q.find("small", class_="author").text
                text_area.insert(tk.END, f"{text}\n—— {author}\n\n")
        else:
            messagebox.showerror("错误", f"状态码: {response.status_code}")
    except Exception as e:
        messagebox.showerror("网络错误", str(e))


# 1. 创建主窗口
window = tk.Tk()
window.title("深渊名言爬虫 - Project Ghost")
window.geometry("600x500")  # 宽 600，高 500

# 2. 创建一个按钮
btn = tk.Button(window, text="开始抓取名言", font=("Arial", 12, "bold"), command=get_quotes)
btn.pack(pady=10)  # pady 表示上下留点空隙b

# 3. 创建一个滚动文本框用来显示结果
text_area = tk.Text(window, wrap="word", font=("Arial", 11))
text_area.pack(expand=True, fill="both", padx=10, pady=10)

# 4. 运行窗口主循环
window.mainloop()
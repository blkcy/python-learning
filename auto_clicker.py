import pyautogui
import time

# 开启防失控机制：鼠标移动到屏幕左上角(0,0)会自动引发异常并停止程序
pyautogui.FAILSAFE = True

print("【警告】请在 5 秒内把鼠标移到安全的地方（比如一个空白记事本）！")
time.sleep(5)

print("开始执行！把鼠标甩到左上角可以紧急停止。")

try:
    while True:
        x, y = pyautogui.position()
        print(f"正在点击坐标: ({x}, {y})")
        pyautogui.click(x, y)
        time.sleep(0.5)

except KeyboardInterrupt:
    print("\n手动终止。")
except pyautogui.FailSafeException:
    print("\n触发防失控机制，程序已安全退出！")
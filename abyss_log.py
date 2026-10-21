name = input("请输入你的名字：")
hours = float(input("请输入探索时长："))

# 先打印那句带名字和时长的提示语
print(f"{name}，你已经在深渊中探索了 {hours} 小时。警告：理智值正在下降。")

# 然后进行条件判断
if hours > 8:
    print("深渊太危险了，立刻回祷告室！")
elif hours >= 3:
    print("状态良好，请继续寻找齿轮。")
else:
    print("你只是在摸鱼吗？")
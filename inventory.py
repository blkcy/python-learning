inventory = []
while True:
    print("---发条深渊战利品系统---")
    print("1. 添加战利品")
    print("2. 查看所有战利品")
    print("3. 退出")
    choice = input("请选择操作：")

    if choice =="1":
        item = input("请输入战利品名字：")
        inventory.append(item)
        print(f"成功收集：{item}")
    elif choice =="2":
        print("当前战利品：", inventory)
    elif choice == "3":
        print("退出系统。")
        break
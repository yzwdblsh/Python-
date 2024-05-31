def hesuan(name, tem, asd="居家隔离"):
    if tem <= 37.5:
        print(f"{name},您的体温小于37.5，体温正常")
    else:
        print(f"{name},您的体温大于37.5，需要隔离，隔离方式为{asd}")


name1 = input("请输入您的姓名")
tem1 = float(input("请输入您的体温"))
type2 = input("请输入您的隔离方式")
hesuan(name1, tem1, type2)

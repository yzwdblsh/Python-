while True:
    answer = input('请输入您要查询的业务\n1、显示当前余额\n2、显示当前的剩余流量，单位为G\n3、显示当前的剩余通话分钟'
                   '\n0、退出当前自助查询系统')
    if answer == '1':
        print('您的当前余额为20元')
    if answer == '2':
        print('您当前所剩流量为20G')
    if answer == '3':
        print('您当前剩余的通话分钟为20分钟')
    if answer == '0':
        print("已退出查询系统")
        break
else:
    print("输入错误")

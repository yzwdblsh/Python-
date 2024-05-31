i = 0
while i < 3:
    use_name = input('请输入您的用户名:')
    pwd = input('请输入您的密码:')
    if use_name == 'ysj' and pwd == '888888':
        print('系统正在登录中，请稍后')
        i = 4
    else:
        if i < 2:
            print('用户名或者密码不正确，您还用', 2 - i, '次机会')
            i += 1
    if i == 3:
        print('三次均输错')

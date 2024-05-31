score = eval(input('请输入您的成绩：'))
if score < 0 or score > 100:
    print('成绩有误!')
elif 0 <= score < 60:
    print('E')
elif 60 <= score < 70:
    print('D')
elif 70 <= score < 80:
    print('C')
elif 80 <= score < 90:
    print('B')
elif 90 <= score < 100:
    print('A')

USER_name = input('请输入您的用户名:')
pwd = input('请输入您的密码:')
if USER_name == 'ysj' and pwd == '888888':
    print('登录成功')
else:
    print('用户名或密码不正确')

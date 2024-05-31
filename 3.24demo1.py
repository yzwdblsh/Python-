pwd = eval(input('请输入年份'))
if pwd % 4 == 0 and pwd % 100 != 0 or pwd % 400 == 0:
    print(pwd, '是闰年')
else:
    print(pwd, '是平年')

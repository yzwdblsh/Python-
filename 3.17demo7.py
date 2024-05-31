answer = input('请问，您喝酒了没?\n请输入yes or no:')
if answer == 'yes':
    proof = eval(input('请输入酒精含量:'))
    if proof < 20:
        print('构不成酒驾，祝您一路平安!')
    elif proof < 80:
        print('已构成酒驾，请不要开车！')
    else:
        print("已到达醉驾标准，千万不要开车!")
else:
    print('你走吧没你啥事')

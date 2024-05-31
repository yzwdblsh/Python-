i = 0
while i <= 15:
    i = i + 1
    print('*', end="")
    if i % 4 == 0:
        print(' ')
print("-------")
a = '*'
i = 0
while i <= 4:
    i = i + 1
    print(i * a, )

print("-------")
a = '*'
i = 6
while i >= 0:
    i = i - 1
    print(i * a, )
print("-------")
a = '*'
i = 5
b = 0
print(5*" "+a)
while i >= 1:
    i = i - 1
    b = b + 1
    print(i * " ", end="")
    if i == 4:
        print((2 * b + 1) * a)
    else:
        print((2*b+1)*a)

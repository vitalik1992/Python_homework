a = input('Введіть символ для контуру : ')
b = input('Введіть символ для заливки : ')
for i in range(0,4):
    if i == 0 or i == 3:
        print(a * 10)
    else:
        print(a,b*6,a)







from random import *
random_list = []
pos_quan = 0
neg_quan = 0
zero_quan = 0
for i in range(0,20):
    x = randint(-5,4)
    random_list.append(x)
    print(x,end=' ')

for i in random_list:
    if i >0:
        pos_quan += 1
    elif i < 0:
        neg_quan += 1
    elif i == 0:
        zero_quan += 1
print('\n' 'Кількість додатних елементів = ', pos_quan,'\n' "кількість від'ємних = ", neg_quan)
print('Кількість нульових елементів = ',zero_quan)

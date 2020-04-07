from random import *
random_pos_list = []
random_neg_list = []
random_list = []

for i in range(0,20):
    x = randint(-5,5)
    print(x, ' ', end='')
    random_list.append(x)

for i in random_list:
    if i > 0:
        random_pos_list.append(i)
    elif i < 0:
        random_neg_list.append(i)
    else:
        pass
print('\n', 'list of positive = ', random_pos_list, '\n' , 'list of negative = ', random_neg_list)

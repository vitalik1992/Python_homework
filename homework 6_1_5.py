from random import *
random_list = []

for i in range(0,10):
    x = randint(-10,10)
    random_list.append(x)
print('Random list =',random_list)

neg_list = []
n = 0
while n < len(random_list):
    if random_list[n] < 0:
        neg_list.append(random_list[n])
    n +=1

for i in neg_list:
    if i in random_list:
        random_list.remove(i)
print('New list = ',random_list)

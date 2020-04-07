from random import *
random_list = []

for i in range(0,10):
    x = randint(-10,10)
    random_list.append(x)
print('Random list =',random_list)

even_list = []
even_list_index = []
i = 0
for i in random_list:
    if i % 2 == 0 and i != 0:
        even_list.append(i)


for i in random_list:
    if i in even_list:
        even_list_index.append(random_list.index(random_list[i]))
print('Even_index_number =',even_list_index)

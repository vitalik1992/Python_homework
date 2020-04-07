from random import *
random_list = []
entered_list = []
result_list = []

for i in range(0,5):
    x = int(input('Enter list element :'))
    entered_list.append(x)
    random_list.append(randint(0,5))
    result_list.append(random_list[i] + entered_list[i])

print('Random list = ',random_list)
print('Entered list = ',entered_list)
print('Result list = ', result_list)

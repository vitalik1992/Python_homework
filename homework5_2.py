counter = 0
number = int(input('Введіть число що більше 2: '))
while number < 2:
    print('Ви ввели число що менше 2')
    number = int(input('Введіть число що більше 2: '))
for i in range(1,10):
    number = int(input('Введіть число що більше 2: '))
    if number % 5 == 0:
        counter += 1
print('Ви ввели %d числа що кратні 5' %(counter))


# Створення списку
from random import *

list1 = []
for i in range(0,5):
    list1.append(randint(0,9))

for i in range(0,5):
    list1.append(chr(randint(32,47)))

for i in range(0,5):
    list1.append(chr(randint(58,127)))
print(list1)
#Поділ на декілька списків
numbers = [0,1,2,3,4,5,6,7,8,9]
number_list = []
letter_list = []
special_char_list = []
for i in list1:
     if i in numbers:
         number_list.append(i)
     elif ord(i) in range(65, 90) or ord(i) in range(97,122):
         letter_list.append(chr(ord(i)))
     else:
         special_char_list.append(chr(ord(i)))

#Конвертація списків в кортежі
number_tup = tuple(number_list)
char_tup = tuple(special_char_list)
letter_tup = tuple(letter_list)

print(letter_tup)
print(number_tup)
print(char_tup)

#Індекс входження символу введеного користувачем в кортежі
user_input = input('Enter your character : ')

if user_input in char_tup:
    print(char_tup.index(user_input))
elif user_input in letter_tup:
    print(letter_tup.index(user_input))
else:
    print(number_tup.index(int(user_input)))

#Реверс кортежу letter_tup
print(letter_tup[::-1])

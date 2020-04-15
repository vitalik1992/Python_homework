# 3. У змінній записаний текст. Словом вважається послідовність непорожніх символів, 
# які йдуть підряд, слова розділені одним або більше пробілом.
# Програмно створіть словник, в якому ключами є слова з речення, 
# а значеннями – кількість входження в речення.

sentence = input('Enter sentence : ')
listt = sentence.split(' ')
new_list= []
for i in listt:
    if i != '':
        new_list.append(i)

new_dict = {}

for i in new_list:
    quantity = new_list.count(i)
    if i not in new_dict:
        new_dict[i] = quantity


for i in new_dict:
    print(i, '=', new_dict[i])

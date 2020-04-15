# 2. Створіть словник, ключами є слова, а значеннями – список слів-синонімів до нього. Програма отримує на вхід кількість слів N. Далі користувач вводить слова-ключі та відповідні йому синоніми.
# Передбачити:


# 1) на запит (слово) користувача вивести список синонімів;
from random import *
sunonyms_dict = {'good' : ['acceptably','alright','fine',' satisfactorily'],
                 'bad': ['bastard',' crummy','lame','wrong'],
                 'believe': ['consider',' trust','conceive','think']}

key = input('Enter word to find synonym : ')
if key in sunonyms_dict:
    new_list = sunonyms_dict[key]
    print('Synonyms for entered word is : ')
    for i in new_list:
        print(i,end=',')
else:
    print('There is no enetered word in dictionary!')

# 2) користувач вводить речення, в якому є слова (ключі, що містяться в словнику).
# Замінити їх синонімами та вивести речення на екран.
print()
sentence = input('Enter sentence: ')
sentence_list = sentence.split(' ')
for i in sentence_list:
    if i in sunonyms_dict:
        synonyms_list = sunonyms_dict[i]
        index = sentence_list.index(i)
        sentence_list[index] = synonyms_list[randint(0,3)]
        new_sentence = ' '.join(sentence_list)
        print('New sentence : ', new_sentence)
    else:
        print('There is no words from dictionary in entered sentence!')

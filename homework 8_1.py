# 1. Створіть словник, зв'язавши його з змінною school, і наповніть його даними, які б відображали кількість учнів в десяти різних класах (наприклад, 1а, 1б, 2б, 6а, 7в тощо.).
# Уявіть, що в школі відбулися зміни, додайте їх в словник:


school = {'1A':15, '1B':17, '1C':19, '2A':16, '3A':20, '3B':19, '4A':12, '4B':20, '5A': 18, '5B': 25}
#Дізнайтеся скільки людей в певному класі.
clas = input('Enter class to get pupils number: ')
if clas in school:
    print(school[clas])
else:
    print('Class does not exist')


# - В трьох класах змінилося кількість учнів;
while True:
    change_class = input('Enter class you want to change quantity of pupils :')

    if change_class in school:
        new_quantity = input('Enter new quantity: ')
        school[change_class] = new_quantity
        print(school)
    else:
        print('There is no entered class!')

    print('Enter "y" to continue or something else to stop : ')
    question = input()
    if question == 'y':
        continue
    else:
        break


# - В школі з'явилося два нових класу;
while True:
    add_class = input('Enter class title you want to add : ')
    pupils_quan = input('Enter quantity of pupils : ')
    school[add_class] = pupils_quan
    question = input('Enter "y" to continue or something else to stop : ')
    if question == 'y':
        continue
    else:
        break
print(school)


# - В школі розформували один з класів.
while True:
    class_id = input('Enter class title you want to delete :')
    if class_id in school:
        school.pop(class_id,'Not exist')
    else:
        print('Entered class does not exist!')
    question = input('Enter "y" to continue or something else to stop : ')
    if question == 'y':
        continue
    else:
        break

# Виведіть вміст словника на екран.
for key in school:
    print('Class %s consist from %d pupils' %(key,school[key]))

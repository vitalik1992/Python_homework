entered_list =[]
for i in range(0,10):
    value = int(input('Enter list element : '))
    entered_list.append(value)
suma = sum(entered_list)

dob = 1
for i in range(0,10):
    dob *= entered_list[i]

print('Ваш список : ', entered_list,'\n' 'Сума елементів : ', suma,'\n' 'Добуток елементів : ',dob)

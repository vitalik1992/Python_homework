number = input('Enter your number : ')
mult = 1
str1 = str(number)
for i in range(0,len(str1)):
    mult *= int(str1[i])
print(str1[::-1])
print('mult = ',mult)





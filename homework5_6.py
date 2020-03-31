counter_pos = 0
counter_neg = 0
counter = 0
while True:
    number = int(input('Enter your number : '))
    if number == 0:
        break
    counter += 1
    if number > 0:
        counter_pos += 1
    else:
        counter_neg += 1
pers_pos = 100 * counter_pos / counter
pers_neg = 100 * counter_neg / counter
print('pers_pos = %.2f%%, pers_neg = %.2f%%' %(pers_pos,pers_neg))




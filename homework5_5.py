counter = 0
sum1 = 0
mult = 1
p = 5
n = 10
while True:
    number = int(input('Enter your number'))
    if number == p or number == n:
        break
    elif number < p:
        sum1 += number
    elif number > n:
        mult *= number
    else:
        counter += 1
print('sum =',sum1,  ' mulp =', mult, ' count = ',counter )







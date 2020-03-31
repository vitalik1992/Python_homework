from random import randint
print('Відгадай число')
number = randint(0,100)

for i in range(0,100):
    user_number = int(input('Твоє число : '))
    if user_number == number:
        print('Ти виграв')
        break
    elif user_number > number:
        print('Твоє число завеликє')
    elif user_number < number:
        print('Твоє число замале')
    i += 1
print('Загадане число: %d' %(number))


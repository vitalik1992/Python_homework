money_amount = int(input('Enter your money emount : '))
if money_amount >= 200:
    quantyty_of_200 = money_amount // 200
    print('Кількість 200 гривневих купюр ', quantyty_of_200)
    money_amount = money_amount - quantyty_of_200 * 200
if money_amount >= 100:
    quantyty_of_100 = money_amount // 100
    print('Кількість 100 гривневих купюр ', quantyty_of_100)
    money_amount = money_amount - quantyty_of_100 * 100
if money_amount >= 10:
    quantyty_of_10 = money_amount // 10
    print('Кількість 10ти гривневих купюр ', quantyty_of_10)
    money_amount = money_amount - quantyty_of_10 * 10
if money_amount >= 1:
    quantyty_of_1 = money_amount // 1
    print('Кількість 1 гривневих монет ', quantyty_of_1)
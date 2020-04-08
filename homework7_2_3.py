string = input('Enter your string = ')
set_small_letters = set()
set_big_letters = set()
set_of_numbers = {0,1,2,3,4,5,6,7,8,9}
big_letters_sorted = set()
small_letters_sorted = set()
set_of_unavailable_numbers = set()
set_of_string_numbers = set()

for i in string:
    if ord(i) in range(65,91):
        set_big_letters.add(i)
        big_letters_sorted = sorted(set_big_letters)

    if ord(i) in range(97,123):
        set_small_letters.add(i)
        small_letters_sorted = sorted(set_small_letters)
    elif ord(i) in range(48,58):
        number = int(i)
        set_of_string_numbers.add(int(i))
        set_of_unavailable_numbers = set_of_numbers.difference(set_of_string_numbers)


print(big_letters_sorted)
print(small_letters_sorted)
print(set_of_unavailable_numbers)

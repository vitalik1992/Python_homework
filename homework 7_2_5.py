string1 = input('Enter your string : ')
string2 = input('Enter your string : ')

set_of_first_str_letters = set()
set_of_second_str_letters = set()
union_letters_set = set()

for i in string1:
    if ord(i) in range(65,91) or ord(i) in range(97,123):
        set_of_first_str_letters.add(i)

for i in string2:
    if ord(i) in range(65,91) or ord(i) in range(97,123):
        set_of_second_str_letters.add(i)

union_letters_set = sorted(set_of_first_str_letters.intersection(set_of_second_str_letters))

print(set_of_first_str_letters)
print(set_of_second_str_letters)
print(union_letters_set)

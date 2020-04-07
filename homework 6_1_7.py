new_list = [1,2,3,3,5,3,7,2,2]

print(new_list)
unique_list = []
for x in new_list:
    if x not in unique_list:
        unique_list.append(x)

print(unique_list)

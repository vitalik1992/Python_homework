import random
random_list = []
random_list = random.sample(range(-10,30),10)
print(random_list)
maxx = max(random_list)
minn = min(random_list)
print(maxx,minn)
index1 = random_list.index(maxx)
index2 = random_list.index(minn)
random_list[index1], random_list[index2] = random_list[index2], random_list[index1]
print(random_list)

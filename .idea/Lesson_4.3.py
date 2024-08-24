import random
lst = []
for i in range(0, random.randint(3,10)):
    lst.append (random.randint(0, 100))
new_lst = []
new_lst.append(lst[0])
new_lst.append(lst[2])
new_lst.append(lst[-2])
print('Згенерований сисок:', lst)
print('Новий список:', new_lst)
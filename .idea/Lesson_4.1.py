lst = [2,0,3,4,5,1,0,132,0,343,5,0,0,888]
print ('Початковий список:', lst)
count = lst.count(0)
count_1 = lst.count(0)
while count >= 1:
    lst.remove(0)
    count = lst.count(0)
for i in range(0,count_1):
    lst.append(0)
print ('Список з нулями в кінці:', lst)
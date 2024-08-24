lst =[2,0,3,4,5,1,0,132,0,343,5,0,0,888]
len = len(lst)
if len > 0:
    # Через функцію суми:
    print (sum(lst[0::2]) * lst[-1])
    # Через те, що вчили:
    suma = 0
    for number in lst[0::2]:
        suma += number
        result = suma * lst[-1]
        continue
    print(result)
else:
    print('0')
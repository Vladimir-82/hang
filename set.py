'''
Сортировка четных чисел массива
Нечетные остаются на своих местах
'''
index_odd_list=[]
odd_numbers_list=[]
index_even_list=[]
even_numbers_list=[]
some_list=[8, 88, 4, 5, 11, 6, 23, 77, 2]
print(some_list)
for i in range(len(some_list)):
    if some_list[i] % 2 != 0:
        index_odd_list.append(i)
        odd_numbers_list.append(some_list[i])
    else:
        index_even_list.append(i)
        even_numbers_list.append(some_list[i])

print('индексы нечетных чисел', index_odd_list)
print('нечетные числа', odd_numbers_list)

#for k in range(1, len(even_numbers_list)):#метод пузырька при сортировке списка четных чисел(можно через sorted)
    #for x in range(len(even_numbers_list)-1):
        #if even_numbers_list[x+1] < even_numbers_list[x]:
            #even_numbers_list[x], even_numbers_list[x+1] = even_numbers_list[x+1], even_numbers_list[x]
#print('отсортированный список четных чисел', even_numbers_list)
even_numbers_list=sorted(even_numbers_list)#через sorted

for i in range(len(odd_numbers_list)):
    even_numbers_list.insert(index_odd_list[i], odd_numbers_list[i])

print('конечный результат', even_numbers_list)

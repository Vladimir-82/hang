'''Программа ищет общий делитель у заданного колличества чисел'''
def deviser(num_list):
    lists=[]
    all_numbers=[]
    inter=[]
    for arg in num_list:
        lists.append([i for i in range(2, arg + 1) if arg % i == 0])

    for i in lists:
        for j in i:
            all_numbers.append(j)
    for i in all_numbers:
        if all_numbers.count(i)==len(lists):
            inter.append(i)

    if len(inter)>=1:
        print(f'Общий делитель у чисел --> {max(inter)}')
    else:
        print('У этих чисел нет общего делителя!')

count_of_numbers=1
while count_of_numbers == 1 or count_of_numbers == 0:
    count_of_numbers=int(input('Введите колличество чисел равное 2 или более:'))

num_list=[]
for i in range(count_of_numbers):
    num=int(input('Введите число:'))
    num_list.append(num)

deviser(num_list)

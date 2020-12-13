
def deviser(*args):
    lists=[]
    for arg in args:
        lists.append(set([i for i in range(2, arg + 1) if arg % i == 0]))
    print(lists)

    inters=set.intersection(lists[0], lists[1])#нужно что-то делать
    print(inters)
    print(max(inters))

count_of_numbers=int(input('Введите колличество чисел:'))#нужно что-то делать
for i in range(count_of_numbers):
    num_list=[]
    num=int(input('Введите число:'))
    num_list.append(num)

deviser(10, 20)


def deviser(*args):
    lists=[]
    for arg in args:
        lists.append(set([i for i in range(2, arg + 1) if arg % i == 0]))
    print(lists)
    print(max(set.intersection(lists[0], lists[1], lists[2])))
num1=30
num2=20
num3=10
deviser(num1, num2, num3)



'''
def deviser(num_1, num_2):
    x1_numbers = [i for i in range(2, num_1+1) if num1 % i == 0]
    x2_numbers = [i for i in range(2, num_2+1) if num2 % i == 0]

    if len(set.intersection(set(x1_numbers), set(x2_numbers))) >= 1:
        print(max(set(x1_numbers) & set(x2_numbers)))
    else:
        print('No divisers')

num1=30
num2=3
deviser(num1, num2)
'''
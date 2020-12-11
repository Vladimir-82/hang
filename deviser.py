def deviser(num_1, num_2):
    x1_numbers = [i for i in range(2, num_1)]
    x2_numbers = [i for i in range(2, num_2)]
    devisers_list_1=[]
    devisers_list_2=[]

    for i in x1_numbers:
        if num_1 % i == 0:
            devisers_list_1.append(i)
    for i in x2_numbers:
        if num_2 % i == 0:
            devisers_list_2.append(i)

    devisers_list_1=sorted(devisers_list_1)
    devisers_list_2=sorted(devisers_list_2)

    for i in range(len(devisers_list_1)):
        if devisers_list_1[i] in devisers_list_2:
            print(devisers_list_1[i])
        else:
            i += 1
    else:
        print('No divisers')

num1=12
num2=8
deviser(num1, num2)
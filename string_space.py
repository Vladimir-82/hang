'''функция переворачивает слова в строке с пробелами,
пробелы остаются на месте'''
def reverse_str(some_string: str):
    print(some_string)

    lst = some_string.split()
    for i in range(len(lst)):
        lst[i] = lst[i][::-1]

    reverse_string = ''
    for i in lst:
        for j in i:
            reverse_string += j

    z = (i for i in reverse_string)

    other_string = ''
    for i in range(len(some_string)):
        if some_string[i]!=' ':
            other_string += next(z)
        else:
            other_string += ' '

    print(other_string)

some_string = ' olleH Hello   '
reverse_str(some_string)
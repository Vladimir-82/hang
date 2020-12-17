def reverse_str(some_string:str):
    lst=some_string.split()
    print(lst)
    for i in range(len(lst)):
        lst[i] = lst[i][::-1]
    print(lst)

    if lst[0][::-1] in some_string:
        print(True)
some_string = '  няхай    беларусь  жыве   вечна   '
reverse_str(some_string)
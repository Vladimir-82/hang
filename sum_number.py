def sum_num(number:str):
    res = sum([int(i) for i in number])
    return res

num=input('input a number:')
print(sum_num(num))
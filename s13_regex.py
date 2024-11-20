# import re
# path1 = 'C:/Users/Mahyar/Desktop/audit.log'
# f = open(path1, 'r',encoding='utf-8-sig')
# readfile = f.read()
# print(readfile)

# a = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',readfile)
# b = re.findall(r'--(.*)-- (.+?) (.+?) (.+?) (.+)\.', readfile)
# print(b)

# c = re.sub(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', 'xxx.xxx.xxx.xxx',readfile)
# print(c)
# ^--(.*)-- (.+?) (.+?) (.+?) (.+)\.


def square(x):
    return x ** 2
#
#
# new_square = lambda x:x**2
#
#
# print(new_square(8))
# print(square(8))


# if condition:
#     return 'True'
# else:
#     return 'False'
#
# lambda x: 'True' if condition else 'False'

# def odd_even(x):
#     if x % 2 == 0:
#         return 'even'
#     else:
#         return 'odd'
#
# # print(odd_even(5))
#
# odd_even_new = lambda x: 'even' if x%2 == 0 else 'odd'
# print(odd_even_new(5))

# map(function, iterable)
list_a = [1, 2, 3, 4, 5, 6]
# doubled_list = map(lambda x: 'even' if x%2 == 0 else 'odd', list_a)
# squared_list = map(square,list_a)
# print(list(squared_list))
even_numbers = filter(lambda x:x%2 == 0,list_a)
print(list(even_numbers))


# name = "Sina"
# print(name[0])
#
# cars = ['Benz', 'BMW']
# print(cars[0])
#
# cars = []
# cars.append('Benz')
# cars.append('BMW')

# en2fa = {"apple": "sib", "hello": "salam"}
# print(en2fa["apple"])
# print(en2fa["hello"])

# en2fa["apple"] = "سیب"
# en2fa["goodbye"] = "khodafez"
# print(en2fa)

# employeeId_username = {}
# # employeeId_username = dict()
# employeeId_username[7328] = "ma.nazari"
# employeeId_username[1010] = 'a.abbasi'
# employeeId_username[1817] = 's.norouzi'
# # employeeId_username['1113'] = 'a.asghari'
#
# print(employeeId_username)

# print(list(employeeId_username.keys()))
# print(list(employeeId_username.values()))
# print(list(employeeId_username.items()))

# if 7328 in employeeId_username:
#     print(True)
# else:
#     print(False)

# text = '100 dane yaghout, daste be daste'
# dict_counter = {}
# for letter in text:
#     count_letter = text.count(letter)
#     dict_counter[letter] = count_letter
#     # print(f'{letter}: {count_letter}')
#
# print(dict_counter)
#
# for item in dict_counter:
#     # print(item)
#     print(f'The word {item} has been repeated {dict_counter[item]} time.')

# username_excel = ['ma.nazari', 's.farsi', 'a.gholami']
# username_telephone = {'ma.nazari': '0912xxxxxxx', 'a.najafi': '0912yyyyyyy'}
#
# for username in username_excel:
#     # if username in username_telephone.keys():
#     #     print(f'{username} is {username_telephone[username]}')
#     # else:
#     #     print(f'{username} is not existed')
#
#     print(username, username_telephone.get(username, "is not existed"))

# list_a = [1,2,3,4]
# list_a[0] = 1000
# # print(list_a)
# # print(list_a[1:3])
# list_a.append(200)
# list_a.remove(2)
# print(list_a)

# tuple_a = (1, 2, 3, 4)
# print(tuple_a)
# print(type(tuple_a))
# print(tuple_a[1:3])
# print(tuple_a[3])
# tuple_a[2] = 3900

# list_b = [2, 3]
# tuple_b = tuple(list_b)
# print(tuple_b[1])
# print(tuple_b)
# list_c = [(2, 3), (5, 6), (9, 10)]
# print(list_c[1][0])

# dict_a = {'ali': 180, "jafar": 160}
# dict_b = {('ali', 'nasiri'): 180, ('jafar', 'masoumi'): 160}
# print(dict_b)
# print(dict_b[('ali','nasiri')])

# name, family = 'mahyar', 'nazari'
# print(name)
# print(family)

# a = (15)
# print(type(a))
#
# b = (15,)
# print(type(b))
#
# c = (,)
# print(type(c))

# def plus_one_and_two(number):
#     plus_one = number + 1
#     plus_two = number + 2
#     return plus_one, plus_two
#
# result = plus_one_and_two(10)
# print(result[0])
# p_1, p_2 = plus_one_and_two(10)
# print(p_1)

food_price = {'pizza': 400, 'pasta': 250, 'lasagna': 350}
# for food in food_price:
#     print(f'{food} is {food_price[food]}T')

# print(list(food_price.items()))
# for food, price in list(food_price.items()):
#     print(f'{food} is {price}T')
    # print(food)
    # print(price)

# name, family = "mahyar", "nazari"

# print(type(list((food_price.items()))))




grade = {'mahdi':20 , 'amin':15 ,'keyvan':19 ,'behzad':11}
z = list(grade.items())
print(z)
z[1][0] = 'raha'



z[1][1] = '18'
#
#
#
z[1] = ('raha',15)

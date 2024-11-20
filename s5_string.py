# text = 'python'
# print(text[10])


# print(len(text))
# for index in range(0, len(text)):
#     print(index, text[index])


# for letter in text:
#     print(letter)

# text = 'The weather is nice'
# counter_i = 0
# for letter in text:
#     if 'i' == letter:
#         counter_i += 1
#
# print(counter_i)

# text = "Today is Saturday"
# print(text[6:8])
# print(text[9:17])
# print(text[9:])
# print(text[:5])
# print(text[-1])
# print(text[-8:])


# name = 'amir'
# print(name[3])
# name[3] = 'n'   ## False
# name_new = name[:3] + 'n'
# print(name_new)

# name = 'asghar'
# print(type(name))

# in
# if 'ghar' in name:
#     print("OK")
# else:
#     print("NOK")

# name_1 = "asghar"
# name_2 = "akbar"
#
# if name_1 > name_2:
#     print("1")
# else:
#     print("2")

# name = 'Asghar'
# print(name.upper())
# print(name.lower())

# name = 'asghar'
# print(name.count('a'))
# print(name.find('g'))
# print(name.find('a'))
# print(name.find('a', 1))

# name = '   asghar   '
# print(name.strip())

# name = "mahyar"
# print(name.startswith("yar"))

# name = "amir"
# name_new = name.replace('r', 'n')
# name_new_2 = name.replace('amir', 'amin')
# print(name_new)
# print(name_new_2)

# name = 'amir reza'
# name = name.title()
# print(name)

# name = 'Zahra'
# code = '1234'
# text = "Im " + name + " with code: " + code
# print(text)
# print("im", name, 'with code:', code)
# text = "Im %s with code: %s" % (name, code)
# text = f'Im {name} with code: {code}'
# text = 'Im {} with code: {}'.format(name, code)
# print(text)

email = input("Enter the email address:\n")
find_at = email.find('@')
print(find_at)
while ('@' not in email or '.' not in email[find_at + 1:]):
    email = input("Enter the email address again:\n")

username = email[:find_at]
domain = email[(find_at + 1):]
print("username=",username)
print("domain=",domain)

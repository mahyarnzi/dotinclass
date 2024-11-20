# l1 = [2, 2.5, True, "Ali"]
# print(l1[2])
# print(l1[-1])
# print(l1[1:3])
# print(len(l1))

# l1[0] = 100
# print(l1)

# l2 = [l1, "Fatemeh", 19.2]
# print(l2)
# print(len(l2))
# print(l2[0][3])

# l3 = [4, 5]
# l4 = ["Sina", "Narges"]
# print(l3 + l4)
# print(l3 * 3)

# l3.extend(l4)
# print(l3)
# print(l4)

# l5 = ["Tehran", "Tabriz", "Mashhad"]
# l5.append("Hamedan")
# print(l5)
# l5.insert(-1,"Shiraz")
# print(l5)

names = []
families = list()
cities = []
l6 = [["Mahyar", "Nazari", "Tehran"], ["Abbas", "Asghari", "Mashhad"], ["Nazanin", "Jamshidi", "Yazd"]]
# for index in range(len(l6)):
#     names.append(l6[index][0])
#     families.append(l6[index][1])
#     cities.append(l6[index][2])
#
# print(f"names: {names}")
# print(f"families: {families}")
# print(f"cities: {cities}")

# for item in l6:
#     names.append(item[0])
#     families.append((item[1]))
#     cities.append(item[2])
#
# print(f"names: {names}")
# print(f"families: {families}")
# print(f"cities: {cities}")

# l7 = ["Solmaz", "Sirous", "Soroush"]
# l8 = [100, 2, 41, 20]
# l7.sort()
# print(l7)
# l8.sort(reverse=True)
# print(l8)

# l9 = ["Daryoush", "Anita", "Azita", "Anoushiravan"]
# del l9[1]
# l9.remove("Azita")
# print(l9)

# l10 = ["Iran", "Japan", "China", "America"]
# selected_country = l10.pop()
# selected_country2 = l10.pop(0)

# print(selected_country)
# print(selected_country2)
#
# print(l10)

# l11 = [8, 3, 21, 4]
# print(max(l11))
# print(min(l11))
# print(sum(l11))
# print(sum(l11)/len(l11))
# print(l11.index(21))

# email = "ma.nazari@dotin.ir"
# email_list = email.split('@')
# username = email_list[0]
# domain = email_list[1]
# print(username)
# print(domain)
#
# text = "Dotin is the best place in the world"
# text_list = text.split()
# print(text_list)

# labels = ["nazari_pc", "akbari_camera", "sasani_pc"]
# count_pc = 0
# for label in labels:
#     name_device = label.split('_')
#     device = name_device[1]
#     if device == 'pc':
#         count_pc += 1
#
# print("pc: {}".format(count_pc))

# l12 = ["mahyar", "nazari", "7328"]
# filename = "_".join(l12)
# print(filename)

# l13 = ["mahyar", "mahsa"]
# if "mahsa" in l13:
#     print("Yes")
# else:
#     print("No")

# a = 'salam'
# b = a
# b = 'a' + b
# print(b)
# print(a)
#
# a = [1, 2, 3]
# b = a
# b[0] = 100
# print(b)
# print(a)

# brain="Know yourself! Understand yourself! Correct yourself!"
# brain=brain.strip()
# # print(brain)
# change=brain.split("yourself!")
# print(change)
# print(len(change))

a = "mahyar@"
print(a.split('@'))
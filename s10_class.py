h1_name = 'Mahyar'
h1_family = "Nazari"
h2_name = 'Ali'
h2_family = 'Akbari'


# class Human:
#     pass_


# h1 = Human()
# h2 = Human()
# h1.name = 'Mahyar'
# h1.family = 'Nazari'
# h2.name = 'Ali'
# h2.family = 'Akbari'
# h2.email = 'a.akbari@dotin.ir'
# print(h1.name)
# print(h2.family)
# print(h1.email)


# p1 = Human()
# p2 = Human()
# # print(p1.count)
# p1.count = p1.count + 1
# print(p1.count)
# print(p2.count)

class Human:
    count = 0
    def __init__(self, name, family):
        self.name = name
        self.family = family
        Human.count = Human.count + 1
        self.count = Human.count

    def set_email(self, email):
        self.email = email

    def fullname(self):
        return f'{self.name} {self.family}'

    def __str__(self):
        return self.name

#
# p1 = Human("Mahyar","Nazari")
# p2 = Human("Sanaz", "Asghari")
# p1.set_email("ma.nazari@dotin.ir")
# print(p1.fullname())
# print(p1.name)
# print(p1.family)
# print(p2.name)

# print(p2.count)

# print(p1)

# class Empolyee(Human):
#     def set_personalcode(self, personalcode):
#         self.personalcode = personalcode
#
#     # def fullname(self):
#     #     return f"{self.name} {self.family} {self.personalcode}"
#     def fullname2(self):
#         # return f"{self.name} {self.personalcode}"
#         return f"{super().fullname()} {self.personalcode}"
#
# e1 = Empolyee("Asghar", "Mohammadi")
# e1.set_personalcode(7328)
# # print(e1.personalcode)
# # print(e1.fullname())
# print(e1.fullname2())

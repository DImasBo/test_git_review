# OPP
# class, -> object
# class - methods, parameters
# __init__ - конструктор описуємо певні зарактеристи або інструкції
# from <name_module> import ClassName
#
# class Person:
#
#     def __init__(self, n):
#         self.name = n
#
#
# p = Person("Dmytro")
# p.name

######
# 3 - принципа ООП
# інкапсуляція
# public, private, property
#
# class Person:
#     # __ - private value
#     __wallet_amount = 100
#     # public
#     name = "Dmytro"
#     #
#     _test = "test"
#
#     def add_money(self, amount):
#         self.__wallet_amount += amount
#
#     def add_account(self):
#         self.__create_password()
#
#     def __create_password(self):
#         self.__password1 = "teste"
#
# p = Person()
# print(p.name)
# p.add_money(100)
# print(p._test)

# успадкуваня

# class Car():
#     type = "sidan"
#     colesa = 4
#
#     def drive_up(self):
#         pass
#
#     def drive_down(self):
#         pass
#
# class Fura(Car):
#     colesa = 6
#     prichep = 5000
#
#
# c = Car()
#
# f = Fura()

# полиморфизм

class Animal:

    def __init__(self, name):
        self.name = name

    def say(self):
        print("say something")


class Dog(Animal):

    def say(self):
        print("Wow")


class Cat(Animal):

    def say(self):
        print("may")


animals = [
    Cat("Marik"),
    Dog("Sirko"),
    Dog("Sirko2"),
    Dog("Sirko3"),
]

for a in animals:
    a.say()
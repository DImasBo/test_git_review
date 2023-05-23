# # # OPP
# # # class, -> objects
# # # class - methods, parameters
# # # __init__ - конструктор описуємо певні характеристи або інструкції
# # # from <name_module> import ClassName
# # #
# # # class Person:
# # #
# # #     def __init__(self, n):
# # #         self.name = n
# # #
# # #
# # # p = Person("Dmytro")
# # # p.name
# #
# # ######
# # # 3 - принципа ООП
# # # інкапсуляція
# # # public, private, property
# # #
# # # class Person:
# # #     # __ - private value
# # #     __wallet_amount = 100
# # #     # public
# # #     name = "Dmytro"
# # #     #
# # #     _test = "test"
# # #
# # #     def add_money(self, amount):
# # #         self.__wallet_amount += amount
# # #
# # #     def add_account(self):
# # #         self.__create_password()
# # #
# # #     def __create_password(self):
# # #         self.__password1 = "teste"
# # #
# # # p = Person()
# # # print(p.name)
# # # p.add_money(100)
# # # print(p._test)
# #
# # # успадкуваня
# #
# # # class Car():
# # #     type = "sidan"
# # #     colesa = 4
# # #
# # #     def drive_up(self):
# # #         pass
# # #
# # #     def drive_down(self):
# # #         pass
# # #
# # # class Fura(Car):
# # #     colesa = 6
# # #     prichep = 5000
# # #
# # #
# # # c = Car()
# # #
# # # f = Fura()
# #
# # # полиморфизм
# # #
# # # class Animal:
# # #
# # #     def __init__(self, name):
# # #         self.name = name
# # #
# # #     def say(self):
# # #         print("say something")
# # #
# # #
# # # class Dog(Animal):
# # #
# # #     def say(self):
# # #         print("Wow")
# # #
# # #
# # # class Cat(Animal):
# # #
# # #     def may(self):
# # #         print("may")
# # #
# # #
# # # animals = [
# # #     Cat("Marik"),
# # #     Dog("Sirko"),
# # #     Dog("Sirko2"),
# # #     Dog("Sirko3"),
# # # ]
# # #
# # # for a in animals:
# # #     a.say()
# #
# #
# # # static method
# # #
# # #
# # # class Person():
# # #     name = "myNAme"
# # #
# # #     @staticmethod
# # #     def test(t1, t2, ):
# # #
# # #         print("Nice to met you")
# # #
# # #
# # # Person.test()
# # # # p = Person()
# # #
# # # # p.test()
# # #
# #
# # #### class method
# #
# # class Person():
# #     hobby = "Плавання"
# #
# #     def __init__(self, name, ):
# #         self.name = name
# #
# #     def show(self):
# #         print(self.name, self.hobby)
# #
# #     @classmethod
# #     def set_default_hobby(cls):
# #         cls.hobby = "Cooking"
# #
# #
# #
# # p = Person("Dmytro")
# # p.show()
# #
# #
# # Person.set_default_hobby()
# #
# # p.show()
# #
# # p2 = Person("Max")
# # p2.show()
# #
# # p3 = Person("Katy")
# # p3.show()
# # #
# #
# # class Person():
# #     hobby = "Плавання"
# #     tools = []
# #
# #     def __init__(self, name, ):
# #         self.name = name
# #
# #     @classmethod
# #     def create_сook(cls, name, level):
# #         obj = cls(name)
# #         obj.level = level
# #         obj.hobby = "cooking"
# #         obj.tools = ["Черпак", "Ніж"]
# #         return obj
# #
# #
# #     @classmethod
# #     def create_builder(cls, name, level):
# #         obj = cls(name)
# #         obj.level = level
# #         obj.hobby = "Builder"
# #         obj.tools = ["Молоток", "Каску"]
# #         return obj
# #
# #
# # c = Person.create_сook("name", "III")
# # print(c.hobby)
#
# # полиморфизм
#
# a = 10
# s = "test"
# print(a+10)
#
# print(a)
# print(type(a))
# # # print(type(s))
#
#
# #
#
# # a = 10
# # print(type(a))
# # print(a+10)
# #
# # b = "test"
# #
# # b += "test2"
# #
# # print(b)
#
#
# class Book:
#
#     def __init__(self, pages):
#         self.pages = pages
#
#     def test(self):
#         print()
#
#     def __add__(self, book2):
#         return Book(self.pages + book2.pages)
#
# # # b = Book()
# # # b.test()
#
# obj1 = Book(50)
# obj2 = Book(150)
# obj3 = obj1 + obj2
# print(obj3)

# #
# #
# class Book:
#     def __init__(self, name, pages):
#         self.name = name
#         self.pages = pages
#
#     def __int__(self):
#         return self.pages
#     def __str__(self):
#         return f"<Book: {self.name}>"
# #
# #
# book = Book("Енеїда", 150)
# print(book)
# book = int(book)
#
# print(book)
# print(type(book))

# #
# # a = 10
# # print(a)
#
# # class M:
# #     pass
# #
# # class M(object):
# #     pass
#
#
#
# class Product:
#     name = "product"
#     price = 10
#     _discount = 0
#     _discountProchent = 10
#
#     def __init__(self, name, price, discount):
#         self.name = name
#         self.price = price
#         self._discount = discount
#
#     @property
#     def discount(self):
#         return self._discountProchent / 100
#
#
#
# p = Product("Кока Кола", 30, 0.1)
# print(p.price)
# print(p.name)
# print(p.discount + 20)


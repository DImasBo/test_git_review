# # # Class, Object
# #
# # # Таким чином, клас — це користувацький тип даних, що
# # # описує те, які властивості й поведінку будуть мати змінні
# # # цього типу і методи
# class Student():
#     age = 0
#     name = "Name"
#     scope = []
#
#     def arg(self):
#         return sum(self.scope) / len(self.scope)
#
#     def add_scope(self, new_scope):
#         self.scope.append(new_scope)
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.test = 12
#
#     def show(self):
#         print(f"Студент: {self.name}, Вік: {self.age}")
#
#
# # А об'єкт — це змінна класу, тобто екземпляр
# # з конкретним значенням цих властивостей.
# d = Student("Dmytro", 23)
#
# print(d.name)
# d.name = "new name"
# print(d.name)
# d.add_scope(10)
# d.add_scope(12)
# d.add_scope(11)
# a = d.arg()
#
# # a = Student("Arte", 18)
# #
# # a.add_scope(11)
# # a.add_scope(11)
# # a.add_scope(11)
# #
# # c = Student("MARK", 18)
# #
# # c.add_scope(12)
# # c.add_scope(12)
# # c.add_scope(12)
# #
# # students = [d, a, c]
# #
# # for s in students:
# #     s.show()
# #     print(s.scope)
#
# #
# # class Box():
# #
# #     def __init__(self, h=10, w=10, l=10, el="m**2"):
# #         self.i = w
# #         self.k = h
# #         self.p = l
# #         self.el = el
# #
# #     def square(self):
# #         return self.i * self.k * self.p
# #
# #
# # b = Box()
# #
# # big_box = Box(5000, 5000, 5000)
# # box1 = Box(1000, 1000, 1000)
# #
# # print("mini box", b.square(), b.el)
# # print("big box", big_box.square(), big_box.el)
# # print("middle box", box1.square(), box1.el)


class Drip():

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self, a2, b2):
        if self.b == b2:
            self.a += a2

    def show(self):
        print("Чисельник a", self.a)
        print("Знаменик b", self.b)


a = Drip(1, 5)

a.show()

a.add(2, 5)

a.show()
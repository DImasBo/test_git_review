# # наслідування
# #
# # class A:
# #     name = "test"
# #
# #     def m(self):
# #         print("test m")
# #
# #
# # class B(A):
# #
# #     def show(self):
# #         self.m()
# #         print(self.name)
# #
# # b = B()
# #
# # b.show()
#
#
# # class Koleso:
# #     r = 10
# #
# # class Motor:
# #     power = 120
# #
# # class Car(Motor, Koleso):
# #     name = "BMW"
# #
# #
# # c = Car()
#
#
# class A:
#
#     def test(self):
#         print("test A")
#
#
# # class B(A):
#
#     def test(self):
#         #super().test()
#         print("test B")
#
#
# b = B()
#
# b.test()


#*----------- Інкапсуляція
#
# class A:
#     t = "t"
#     __password = "ttesrevsdfvsd"
#
#     def test(self):
#         print("test")
#
#     def test(self):
#         self.__my_secret()
#         self.__password
#
#     def __my_secret(self):
#         print("я маю секрет ...")
#
#
# a = A()
#
# print(a.t)
# a.test()
#
# class P:
#     _t = "t"
#
#     def _test(self):
#         print("protect")
#
#
# p = P()
# p._test()
#
#
# print(p._t)
#
# p._t = "test12"
#
# print(p._t)

# наслідування
#
# class A:
#     name = "test"
#
#     def m(self):
#         print("test m")
#
#
# class B(A):
#
#     def show(self):
#         self.m()
#         print(self.name)
#
# b = B()
#
# b.show()


# class Koleso:
#     r = 10
#
# class Motor:
#     power = 120
#
# class Car(Motor, Koleso):
#     name = "BMW"
#
#
# c = Car()


class A:

    def test(self):
        print("test A")


class B(A):

    def test(self):
        #super().test()
        print("test B")


b = B()

b.test()

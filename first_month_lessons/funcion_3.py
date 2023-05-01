
# sum manual
# name = "Dmytro"  # global var
# a = 0  # global var
#
#
# def hi():
# #    a = 10  # local var
#     global a
#     a+=1
#     print("hello", name)
#
#
# hi()
# print(a) # error

#


def factorial_calc(n):
    if n == 0:
        return 1

    return n * factorial_calc(n-1)


a = factorial_calc(3)
print(a)

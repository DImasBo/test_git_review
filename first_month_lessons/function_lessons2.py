# print("test0", "faffsd")


# import random
#
#
# print(random.randint(0, 10))
#


# def my_sum(a, b, c):  # a, b, c, parameters невизначині
#    print("SUM:", a, b, c)
#    print(a + b + c)

# my_sum(1, 2, 3) # 1, 2 ,3 - аругменти
# my_sum(1, 8, 3)
# a = 1
# b = 2
# c = 3
# my_sum(a, b, c)


# def calc(a, b, c):
#     print("a", a)
#     print("b", b)
#     print("c", c)
#     print(a + b * c ** 2)
#
#
# calc(1, c=3, b=2)

#
# x=1
# x2=2
# calc(x, x2, 5)
#
# x3 = 3
# calc(x, x3, 3)


# print(1,2,3,23,23,23,23, sep="-")
#


def calc(*args, operation="*"):
    if operation == "*":
        r = 1
        for i in args:
            r *= i
        return r

    if operation == "+":
        r = 1
        for i in args:
            r += i
        return r


def print_list(l):
    for item in l:
        print(item)


a = calc(12, 12, 12, 12, )
b = calc(12, 2, 2, 2, )

l = [a, b]

print_list(l)

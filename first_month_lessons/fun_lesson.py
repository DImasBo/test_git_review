# Function

#print("dszasa")
#print("asas")
#print("asasa")
#print("asas     sa")
#print("dszasa")
#max([12,12,12,1232,23,23])
#print("str".lower())

#
# def print_hello(name, ago):
#     print("===========")
#     print("Hello, {n}!!!!".format(n=name))
#     print(ago)
#     print("==========")
#
#
# print_hello("Dmytro", 12)
#
# n = "Dmytro2"
# print_hello(n, 12)
#
# print_hello("Max", 12)
#
#
# def dobutok(a, b):
#     r = a*b
#     return r
#
#
# a = dobutok(4, 3)
# print(a)#, a1, a2)

# def dobutok(a, b):
#     r = a*b
#     return r
#
#
# def traffic_light(color):
#     if color == "RED":
#         return "STOP"
#     elif color == "YELLOW":
#         return "GET READY"
#     elif color == "GREEN":
#         return "GO!!!!!!!"
#     return "Я не знаю що робити на цей колір"
#
#
# a = traffic_light("RED")
# print(a)
#
# print(traffic_light("BLUE"))
#
# def print_odd_numbers():
#     start = int(input("Введіть перше число: "))
#     end = int(input("Введіть друге число: "))
#     for num in range(start, end+1):
#         if num % 2 != 0:
#             print(num)
#
# print_odd_numbers()


# c = input("ведіть символ: ")
# count = int(input("кількість: "))
# is_vertical = bool(input("якщо вертикально ведіть 1, якшо горизонтально 0"))
#
#
# print_line(c, count, is_vertical)



# def mySum(a,b):
#     s = 0
#     for i in range(a,b):
#         s +=i
#     return s
#
# result = mySum(1, 5)
# print(result)


# def print_line(c, count, is_vertical=True):
#
#     if is_vertical:
#         for i in range(count):
#                 print(c)
#     else:
#         print(c*count)


#print_line("*", 5,)
#print_line(c="*", is_vertical=False, count=10)
#print_line("*", is_vertical=False, count=10)


#def p(*args):
#    for i in args:
#        print(i)


#p(10,12,12,12, )
#p()


#def t(**kwargs):
#    print(kwargs)
#    print(kwargs['a'])


#t(a=1,b=2,c=3)
#
# def atc(a, *args, **kwargs):
#     print(a, args, kwargs)
#
# atc(12,12,12,12121,key=1, key2=2)


#def inc_f(a):
#    return a+5

#inc = lambda a: a != 10


#print(inc_f(5))
#print(inc(5))
#
# a = [
#     [1,2,3,4],
#     [3,2,3,4],
#     [2,2,3,1],
# ]

#def eq(a):
#    print(a)
#    return a[-1]

# a.sort(key=lambda a: a[-1])
#
# print(a)


#a = lambda a,b: sum([a,b,1212,12,12,12,])
#a = open("test.html", "w", encoding="utf-8")
# w, a, r

# f = open("test.html")
#
# a = f.read()
# print("a", a)
# f.close()

#
# with open("new_file.html", "a") as f:
#     a = f.write("Test")
#
# print(a)

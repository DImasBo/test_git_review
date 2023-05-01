#
#
# a = "----It step----"
# print(a)
# print(a.lstrip("-"))
# print(a.rstrip("-"))
# print(a.strip("-"))
#
# # print(a.center(60))
#
# # print(a.strip())
# # print(a.split())

# ========================= list ================

# a = [12, 12, 12, 12, 11, 10, 10, 10, 10]
# t = [10.2, 10.5, 10.5]
# test = [12, 12, "Text"]

# print(a)
# print(students)
# print(t)
# print(test)

# 1) create
# students = ["Alex", "Mark", "Katy", "Tania"]
#            #  0,       1,      2,      3   - index
# # # CRUD
# c _CREAT
# # 1) create
# R _read
# # 2) read
# R _UPDATE
# # 3) append item
# # 5) edit item
# D _DELETE
# # 4) remove item
# # 2) read
################
# # print(students)
# print("Hi", students[0])
# print(students[1:3])
# print(students[1], students[3])

# print("Hi", students[1])
# print("Hi", students[2])
# print("Hi", students[3])
# a = [12, 12, 11, 10]
#
# print(a[2])

# 3)  add

a = [12, 12, 11, 10]
#     0   1  2
# print(a)
# # a.insert(2, 9)
# a.insert(2, "9")
# print(a)

# # a.append(9)
# # a.extend(
# #     [1, 2, 3]
# # )
#
# print(a)

# 4) remove

# students = ["Alex", "Mark", "Katy", "Tania"]
# print(students)
#
# i = students.index("Katy")
#
# print(i, students[i])
#
# del(students[i])
# print(students)
#


#  5) edit item
# students = [12, 11, 10, 9, ]
#  0   1   2   3
#         -2   -1

# print(students)
# a = 9
# a = 11
# students[3] = 11
# students[3] = 11
# students[1] = 12
# print(students[3])
# print(students[-1])
# print(students[-2])

# show all
# students = [12, 11, 10, 9]

students = ["Alex", "Mark", "Katy", "Tania"]
# 0        1         2      3
students.append("Bob")

# for item in students:
#     print("Hi", item)
#     if item == "Alex":
#         item = "Alex2"
#     print(item)
# print(students)
# for i in range(len(students)):
#     print(i, students[i])
#     if students[i] == "Alex":
#         students[i] = "Alex2"
#
# print(students)

# обєднати!
# a = [1,2,3,4]

# b = [5,6,7]
# 0 1 2
# print(a[1])

# b[2] = 1
# b[len(b) - 1] = 1
# b[-1] = 1

# print(len(b))

# for item in b:
#     print(item)

# c = a + b
# print(c)


##########################
###### part 2

# b = [
#     # 0         1
#     ["Artem", "Mark"],  # 0
#     # 0        1         2
#     ["Katy", "Alex", "Artem"],  # 1
# ]
#
# print(len(b))
# print(b[0][0])
# print(b[0][1])
# print(b[2])


# обєднання
# a = [1,2,3,4]
# b = [5,6,7]
# c = [8,9,10]
#
# print(a)
# a = a + b + c
#
# print(a)
# print(b)
#
# a = [0] * 100
# print(a)

# a = [[12, 12, 12], ] + [[0, 0, 0, 0]] * 100
# print(a)
#
# a = ["It", "st", "ep"]
#
# print(a)
#
# a[0:2] = ["IT", "ST", 11]
#
# print(a)

# a = [1,2,3,4,5]
#
# L = [6,7,8,9,10]
#
# a.extend(L)
# #print(a)
# a.append(6)
# print(a)


# a.insert(3, 4)
# print(a)

# a = [1,12,12,12,1, 4, 4,34,12,12,12,12,]
# 0  1 2  3  4  5
# val, start, end

# print(a.count(12))
# print(a.count(1))
# print(a.count(0))
# i = a.index(0)
# if 12 in a:
#     i = a.remove(12)
# print(a)
# print(i)
# print(a[i])
# i = a.index(4, 6, -4)
# print(i)

# a.remove(4)
# val = a.pop(5)
# print(a)
# print("Видалено елемент зі значенням", val)


# a = [12,1,2,3,5,11,10]
#
# print(a)
#
# a.sort(reverse=True)
#
# print(a)
# print(a[1])
#

# a = ["Mark", "Alex", "AAAlex", "Bob"]
#
# print(a)
#
# a.sort()
#
# print(a)
#
# a.sort(reverse=True)
#
# print(a)

# students = ["Mark", "Alex", "AAAlex", "Bob", "sdsd"]
# a = [12, 9, 11, 10, 6, 12]
# print(max(a))
# print(min(a))
# print(sum(a) / len(a))

# b = sorted(a, reverse=True)
# print(b)
# print(a)
# a1= 1
# b2 = a1

#
# a = [12, 12, 11, 9, 13]
# # b = a
# # b = a.copy()
#
# print(a)
# #print(b)
# a[0] = 1
#
# print(a)
# print(b)



import random

nums = []
for i in range(100):
    nums.append(random.randint(-100, 100))

print(nums)



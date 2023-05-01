# repit


# a = ["test", ]
# 0
# a.append("test2")
# print(a)
# a.extend(["i1", 1, 2, 3])
# print(a)
# a.insert(3, "newItem")
# print(a)
#
# del(a[1])
# print(a)
# k = a.pop(1)
# print(k)
# print(a)
#
# a.pop()
# print(a)

# a.remove('test')
# print(a)
#
# b = a.copy()
# print("a list", a)
# print("b list", b)
# a = [1,2,3,1,1,1,1]
# print(sum(a))
##print(len(a))
# print(max(a))
# print(min(a))
# b = sorted(a)
# a.sort()
# a = sorted(a)
# print(a)

# print(b)
# print(a)
# print(a.count(1))

# a.reverse()

# print(a)
# a.sort(reverse=True)
# print(a)

# ==================
# tuple - Кортеж

# a = [12, 12, 43, 34, 64,]

# a1 = (12, 12, 43, 34, 64)
# print(a1)

# a2 = 11, 12, 121, 12, 12, 112, 12
# print(a2)
# a2 = (1212 + 1212, 121212, 12, 1212, 121)
# print(a2)
# print(type(a2))
# a_list = [12,12,12,12,12,12,12]
# a_list.append(121)
# a_list.append(1,)
# a_list.pop(1)

# print(a_list)

# a2 = tuple(a_list)

# print(a2)

# a1 = ("12, 12, 43, 34, 64,", 12, 12, True, (112, 12, 12))

# print(a)
# rint(a1)

# print(a.__sizeof__())
# print(a1.__sizeof__())


# a = (12, 12, 12, 12, 12, 45, 345,)
# 0  1   2   3   4    5     6

# print(a.count(12))
# print(a.index(45))
# print(a[1])
# print(a[1: 3])
# print(a)
# print(min(a))
# print(max(a))
# print(len(a))
# print(sum(a))

# print(a[5])
# print(a[6])


# print(a)

# a = (12,12,12,12,)

# print(a)
#
# import random
#
#
# a = [random.randint(-50, 50) for i in range(100)]
#
# print(a)
# a = tuple(a)
# print(a)
#
# s= 0
# for item in a[:5]:
#     s += item
#     print(item)

#
# a = (1,12,23,34,45,6,76)
#
# print(a)
# a_list = list(a)
# a_list.append(1212)
# print(a_list)
# 1) Створити кортеж a = ("Alex", "Katy", "Mark", "Katy") Порахувати скільки разів зустрічається Katy. 
# перетворити В список. Показати що це список. Додати 3 нових слова перетворити в кортеж. 
# вивести на екран кожний елемент.(через цикл)
#
# a = ("Alex", "Katy", "Mark", "Katy")
# print(a.count("Katy"))
#
# a_t = list(a)
# print(type(a_t))
# a_t.append("Max")
# a_t.append("Bob")
# a_t.append("Dmytro")
#
# #a_t.extend(["Max", "Bob", "Dmytro"])
#
# a = tuple(a_t)
#
# for item in a:
#     print(item)
#
########################## Dict #################

#
# user = {
#     "first_name": "Dmytro",  # key: value
#     "ago": 22,
#     "nickname": "DimasBo",
#     "email": "example@gmail.com",
#     "items": ["Пістолет", "Ніж", ],
#     "phone": {
#         "vodafone": "+380501212121",
#         "kievstar": "+380631212121"
#     }
# }
# int, float, bool, None,
# list, tuple, dict,
#
# print(user)
# user.clear()
# print(user)
# print(user["nickname"])
# print(user.get("nickname2"))


#
# user["nickname"] = "DimasNew"  # edit
#
# print(user)
#
# user["phone"] = "+3850042023023"  # if key not exist so add new item
#
#
# a = {
#     "car": "axdfasdfasdf",
# }
#
# print(a)
# print(a)
# a.update({
#     "car": "Автомобіль",
#     "pc": "ПК",
#     "phone": "Телефон",
# })
#
# print(a)
# print(a.keys())
# print(a.values())
#
#

#
# print(rykzak["books"])


# phone.update(option)

# phone["option"] = option
# print(phone)

# for key, val in phone.items():
#     print(key, "-",  val)

# for val in phone.values():
#    print(val)
#
# print(list(phone.values()))
# print(list(phone.keys()))
#
# phone = {
#     "name": "iphone X",
#     "озу": 4,
#     "memory": 125,
# }
#
# option = {
#     "ширина": 13,
#     "довжина": 7,
#     "висота": 0.7,
# }

# c = phone | option | {"test": "test", "tests": 1}
# print(c)


#
# a = {"1": 1, "asd": 2}
#
# b = a.copy()
# print(a)
# print(b)
#
#
#
#
#
#
# repit/ tuple

# a = (12,12,14,12,1,12,12,12,12,12)

# print(a)
# print(a[2])
# print(sum(a))
# print(a.index(14))

# slice [start: stop: step]

# for item in a[2::1]:
#    print("-----", item)
#    item.

# print(a["key"].__hash__())


# a = {
#     "w": 100,
#     "h": 200,
#     "name": "Testssdfvafd"
# }
#
#
# for key, val in a.items():
#     print(key, val)
#
# str,int.float, bool, ()
#user = {
#    "test": 1212, #
#    1: 1212,
#    3: "1212",
#    3.12121: "tests",
#    True: "True",
#    (1, 2, 3, 4): "test"
#}

#print(user["test"])
#print(user[1])
#print(user[3])
#print(user[True])
#print(user[(1, 2, 3, 4)])

#sum_name = input('sub_name: ')
#
# student1 = {
#     "name": "Dmytro",
#     "sub_name": "Bondar",
#     "age": 22,
# }

#
# student2 = {
#     "name": "Alex",
#     "sub_name": "Kovalenko",
#     "age": 18,
# }
# students = [
#     student1,
#     student2,
#     {
#         "name": "Katy",
#         "sub_name": "Kovalenko2",
#         "age": 19,
#     }
#]
#
# print(students[0])
#
# for student in students:
#     print(student["name"])
#     print(student["age"])
# Завдання 1
# Створіть програму, що містить інформацію про відомих
# баскетболістів. Збережіть ПІБ та зріст кожного баскетболіста. Реалізуйте можливість додавати, видаляти, знаходити та
# змінювати дані. Використовуйте словник для збереження
# інформації.

leads = [
    {
        "Імя": "Майкл",
        "Прізвище": "Джордон",
        "Побатькові": "Степанович",
        "зріст": 190,
    },
    {
        "Імя": "Майкл",
        "Прізвище": "Джордон2",
        "Побатькові": "Степанович",
        "зріст": 190,
    }
]
# додавати, видаляти, знаходити та
# # змінювати дані.
print("1) додавати, 2)видаляти, 3)знаходити та 4)змінювати дані 5) q - Для виходу")

while True:
    action = input("Ваша дія: ")
    if action == "1":
        new_name = input("Імя")
        new_name2 = input("Прізвище")
        new_name3 = input("Побатькові")
        w = int(input("Зріст"))
        leads.append({
                "імя": new_name,
                "Прізвище": new_name2,
                "Побатькові": new_name3,
                "зріст": w,
            })
    elif action == "2":
        for i, lead in enumerate(leads):
            print(i, lead['Прізвище'])
        index = int(input("за яким номером видалити баскетболіста"))
        print(index)
        l = leads.pop(index)
        print("Баскетболіст був видаления", index, l)
        print(leads)
    elif action == "4":
        for i, lead in enumerate(leads):
            print(i, lead['Прізвище'])
        index = int(input("за яким номером змінити баскетболіста"))

        new_name = input("Імя")
        new_name2 = input("Прізвище")
        new_name3 = input("Побатькові")
        w = int(input("Зріст"))
        leads[index] = {
            "імя": new_name,
            "Прізвище": new_name2,
            "Побатькові": new_name3,
            "зріст": w,
        }
    elif action == "3":
        search_name2 = input("Ведіть прізвище:")
        for i, lead in enumerate(leads):
            if lead["Прізвище"] == search_name2:
                print(i, lead)


    elif action == 'q':
        break

    print(leads)

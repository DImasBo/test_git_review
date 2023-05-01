
# f = open("files/text.txt")
# #"C:/user/nix/Робочий стот/text.txt"
# print(f)
#
# # print(a)
# # printz(a)
# # for i, student in enumerate(a):
# #     print(i, student)
#
# f.close()

# f.write("Тест нова інформація!\n")
# f.write("\t\tТест нова інформація1!\n")
# f.write("C:\\user\\nix\\Робочий стот\\text.txt\n")
# f.write("Тест нова інформація!")

# f.write("""Тест нова інформація!\n\t\tТест нова інформація1!\nC:\\user\\nix\\Робочий стот\\text.txt\nТест нова інформація!""")
#
# f.write("""Тест нова інформація!
# \t\tТест нова інформація1!
# C:\\user\\nix\\Робочий стот\\text.txt
# Тест нова інформація!""")

#
# import random
#
# a = [random.randint(1,12) for i in range(10)]
# print(a)
#
# for i in a:
#     f.write(str(i) + " ")

#f = open("points.txt", "w", encoding='utf-8')


#f.close()

# f = open("files/text.txt")
#
# for line in f:
#     print(line)
#
# f.close()

# r -read
# w - write
# a - add
# b - binary

with open("pw/text.txt", "a") as f:
    f.write("Новий Студент\n")

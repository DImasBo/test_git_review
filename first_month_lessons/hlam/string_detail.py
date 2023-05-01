# string -

#a = 'My name Dmytro'
#a2 = "I'm Dmytro"

#a3 = 'Im "Dmytro" '

# a4 = """Test Itstep
# asdfasl,sd;l,f;lasd,f
# asdf;lsdm,;flas,d;fl,sldfa
# asdfas;lm,sd;lf,asdf
# """

#print(a)
#print(a2)
#print(a4)


# a3 = "It Step asdfwfаівпфівафіва цайц1234123412341234"
#?????????????dasfasdfs????????????
    # 0123456

# print(a3)
# for i in a3:
#     if ord(i) > 96 and ord(i) < 123: #
#         print(i, ord(i))
#     else:
#         print(i, "не підходить")


#myStr = "12345Python was created in the late 1980's by Guido van Rossum. Python- cool!"
        #0123456789

# slice [start: stop: step]
# print(myStr[:15])
# print(myStr[2:])
#
# print(myStr.find("Python", 100, 150))
# print(myStr.count("Python"))
# print(myStr.rfind("Python"))
#print(myStr.index("Guido2"))


# print(a.lower())
# print(a.upper())
# print(a.title())
# print(a.swapcase())
# print(a.capitalize())



# a = "It Step??"


#if a.endswith("!"):
#    print("Кличне")
#if a.endswith("???"):
#    print("Запитання")
#if a.startswith("It"):
#    print("починається на IT")

#a = "Test 1212122"

#print(a.isalnum())
# a = "ПВАВАПВАВА"
#print("test12".isalnum())
#a = "12кл"
#print(a.isdigit())
#a = "it step It"
#print(a.islower())


#password = input("")
#password = input("")
# потрібно перевірити щоб пароль мав латинські літери або цифри
# і також перевірити чи є символ "#" в кінці рядка
# пароль валідний
# password[:-1].

#password = input("password: ")
# asdfasdfasdf1231341241#

#if password.endswith("#") and password[:-1].isalnum():
#    print("Пароль коректний")
#else:
#    print("Пароль не коректний")

#1.4.5. Методи форматування рядків

#t2 = t.upper().center(30)
#print(t)
#print(t.center(5, "*"))
#print(t.ljust(30, "="))
#print(t.rjust(30))

#t = "************it step*****"
#print(t)#.#lstrip("*"))
#print(t.lstrip("*"))
#print(t.rstrip("*"))
#print(t.rstrip("*").lstrip("*"))

#t = "************it step*****"
#t = "************it step*****"
#print(t.replace("step", "APP"))
#print("12 21 12 12 12 12 12 12".split())
#print("Max-Katy-Artem".split("-"))

#a = input("ведіть через пробіл імена студентів")
#students = a.split()

#print(students)

#for item in students:
#    print(item)
#a = "Hello"

#b = input("name:")

#c = a + " " + b
#name = "ItStepBot"

#c = "Hello {}. I'm telegram bot {}".format(b, name)
#print(c)

#n = "Dmytro"
#ago = 22
#sd = [121212,12,12,12,12] # str(sd) -> "[121212,12,12,12,12]"
#print("My name {}. I am {}. I am python developer!".format(n, ago))
#print("My name {}. I am {}. I am python developer! {}".format(n, ago, sd))
#print("My name {1}. I am {0}. I am python developer! {2}".format(ago, n, sd))
#print(
#    "My name {name}. I am {ago}. I am {profecia}!")
# print(
#    "My name {name}. I am {ago}. I am {profecia}!".format(name=n,ago=ago, profecia="python developer"))

# a = "My name {name}. I am {ago}. I am {profecia}!"
# print(f"My name {n}. I am {ago}")

#print("My name %s. I am %d. I am %s!" % ("Bob", 15, "Java Developer"))
#print("My name " + n + ". I am " + str(ago) +". I am "+"Java Developer"+"!")
#myStr1 = "You have {:>10f} points."
#print(myStr1.format(100002.121212)) #You have 12
##print(myStr1.format(102)) #You have 12
#print(myStr1.format(12)) #You have 12

#a = "12,12,12,12,12asd,sdaf,asdfas".split(",")
#a = ["Katy", "ItStep", "MyStat"]

#b = str(a)

#print(b)
#print(type(b))
#print(",".join(a))
#print("test"[::-1])
#print("asdsdasd\\test")



# Повторення
#
# s = "ItStep"
#     #012345
#
# print(s)
#print(s[3])
#print(s[-1])

# s = 'asdfasd'
# s2 = "asdfasd"
# s3 = """asdfasdf
#     sdafasdfas
# sdfasdfasdf
# asdfasdf
# """

#print(s3)
#a = "121212"+ "dasdfasd"+"  "+ "!"*5
#print(a)
#1 Методи пошуку підрядка в рядку -
# find, index, rfind, rindex, count
# ФОрматування
# upper lower , capitalise, center, swapcase
# Перевірки - True, False
# isdigit, endswitch

#i = input("В")
# Завдання 2
# Користувач вводить з клавіатури деякий текст, а потім —
# список зарезервованих слів. Знайдіть в тексті всі зарезервовані слова та
# змініть їх регістр на верхній. Виведіть на екран
# змінений текст.

text = input("Ведіть з клавіатури деякий текст: ")
string_words = input("список зарезервованих слів(Ведіть слова через пробіл): ")

string_words = string_words.lstrip(" ")
string_words = string_words.rstrip(" ")

words = string_words.split(" ")
print(words)

for word in words:
    text = text.replace(word, word.upper())

print(text)
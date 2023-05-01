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

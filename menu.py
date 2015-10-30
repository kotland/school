import json
from utilities import search, get_full_name, location, clear

school_data = []
students_data = []


def load_data():
    global school_data
    global students_data

    with open(location('data/school.json')) as f:
        school_data = json.load(f)

    with open(location('data/Students.json')) as f:
        students_data = json.load(f)


def menu_do(menu, **kwargs):
    while True:
        clear()
        print("*" * 24)
        print("* Welcome to %s %s *" % (school_data['number'], school_data['type']))
        print("*" * 24)
        print("MENU > ", kwargs.get("sub_menu", ''))
        for number, el in enumerate(menu):
            print("%s. %s" % (number, el["text"]))
        choice = int(input(": "))
        if menu[choice].get("do"):
            if menu[choice]["do"]():
                break
                # break
        else:
            menu_do(menu[choice]["sub_menu"], sub_menu=menu[choice]['text'])
            # return True


def about_students():
    for class_room in school_data["classes"]:
        print("Ученики '%s' класса: " % class_room)
        for student in search(students_data, class_room=class_room):
            # FIXME: учесть(во всей программе), в файле могут быть ученики из других школ
            print("     ", get_full_name(student))  # TODO: Добавить нумерацию учеников для каждого класса
        print("-" * 24)
    input("Нажмите Enter для возврата в предыдущее меню")


def about_classes():
    print("Все классы нашей школы")
    print("||", " || ".join(school_data['classes']), "||")
    print()
    input("Нажмите Enter для возврата в предыдущее меню")


# def info_students():
#     for class_room in school_data["classes"]:
#         print("Ученики '%s' класса: " % class_room)
#         for student in search(students_data, class_room=class_room):
#             # FIXME: учесть(во всей программе), в файле могут быть ученики из других школ
#             print("     ", get_full_name(student))  # TODO: Добавить нумерацию учеников для каждого класса
#         print("-" * 24)
#     input("Нажмите Enter для возврата в предыдущее меню")


def edit():
    print("Menu > Edit")
    input("Нажмите Enter для возврата в предыдущее меню")
    pass


def end():
    global run
    print("Goodbye")
    run = False
    return True


load_data()

menu = [
    {
        "text": "Информация",
        # "do": info,
        "sub_menu": [
            {
                "text": "О классах",
                "do": about_classes
            },
            {
                "text": "Об учениках",
                "do": about_students
            },
            {
                "text": "назад",
                "do": lambda: True
            }
        ]
    },
    {
        "text": "Редактировать",
        "do": edit
    },
    {
        "text": "Выход",
        "do": end
    }
]

run = True

while run:
    menu_do(menu)

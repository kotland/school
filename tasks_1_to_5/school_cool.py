# ctrl+alt+L - форматирование словаря
import os
import json

# def save(data, file_name):
# file = open(os.path.join(DIR, file_name), 'w', encoding="UTF-8")
# file.write(json.dumps(data, ensure_ascii=False))
# file.close()

# h = input("Введите желаемое данных видение: У, Пр, У кл 'number', Сп шк")

stud = open(os.path.join('data', 'Students.json'))
teach = open(os.path.join('data', 'Teachers.json'))
stud_new = open(os.path.join('data', 'Students_new.json'))
teach_new = open(os.path.join('data', 'Teachers_new.json'))

students = json.load(stud)
teachers = json.load(teach)
students_new = json.load(stud_new)
teachers_new = json.load(teach_new)

ls = []
z = {}
surnames = []
lstt = []

for Stud_new in students_new:
ii = 0
ii = ii + 1
Stud_new


print("*"*20, 1, "*"*20)##########################################################################

for Stud_new in students_new:
print(Stud_new['name'])

print("*"*20, 2, "*"*20)##########################################################################

for Teach in teachers_new:
print(Teach['name'])

print("*"*20, 3, "*"*20)##########################################################################

for Stud_new in students:
clss = "5 А"
i = 0
i = i + 1
print(students[i]['name'], students[i]['surname'])
if i > len(Stud_new):
break

print("*"*20, 4, "*"*20)##########################################################################

for Teach in teachers:
print(Teach['school'])

print("*"*20, 5, "*"*20)##########################################################################

for Stud_new in students:
surnames.append(Stud_new["surname"])

namesakes = [surname for surname in surnames if surnames.count(surname) > 1]
print(namesakes)

print("*"*20, 0, "*"*20)##########################################################################

print("*"*18, "Блок 3", "*"*17)

print("*"*20, 1, "*"*20)##########################################################################
print("*"*18, "Готов", "*"*18)

DIR = "data"

students_data = json.load(open(os.path.join(DIR, 'Students.json'), 'r')) # os.path.join - Вставляет нужный \





















# Этап-1: Чтение и обработка данных
import json
import os


def get_teacher(teacher_str, teachers_data):
    """
    Ищет и возвращает словарь с заданным учителя в списке
    :param teacher_str: "Имя Фамилия"
    :param teachers_data: [{"name": "Имя", "surname": "Фамилия", ...}, {...}, ...]
    :return: {"name": "Имя", "surname": "Фамилия", ...}
    """
    name, surname = teacher_str.split(" ")
    for teacher in teachers_data:
        if teacher["name"] == name and teacher["surname"] == surname:
            return teacher


def get_student(student_str, students_data):
    """
    Ищет и возвращает словарь с заданным учеником в списке
    :param student_str: "Имя Фамилия"
    :param students_data: [{"name": "Имя", "surname": "Фамилия", ...}, {...}, ...]
    :return: {"name": "Имя", "surname": "Фамилия", ...}
    """
    name, surname = student_str.split(" ")
    for student in students_data:
        if student["name"] == name and student["surname"] == surname:
            return student


def get_full_name(people):
    return "%s %s %s" % (people["name"], people["middle_name"], people["surname"])


DIR = 'data'

students_data = json.load(open(os.path.join(DIR, 'Students.json'), 'r'))
teachers_data = json.load(open(os.path.join(DIR, 'Teachers.json'), 'r'))

# Задача 1.3
class_room = "6 А"
student_in_class = ['%s %s' % (student["name"], student["surname"]) for student in students_data if student["class"] == class_room]
#**************
student_in_class = []
for student in students_data:
  if student["class"] == class_room:
    student_in_class.append(student)
#**************
print("1.3. Список учеников из", class_room, " -->", student_in_class)

# Задача 1.4
schools = list(set(map(lambda student: student["school"], students_data)))
print("1.4. Список всех школ -->", schools)

# Задача 1.5
surnames = [student["surname"] for student in students_data]
same_surnames = [surname for surname in surnames if surnames.count(surname) > 1]
namesakes = ["%s %s" % (student["name"], student["surname"]) for student in students_data # %s %s - форматирование строки(на место %s встанет слово)
             if (student["surname"] in same_surnames)]
print("1.5. список однофамильцев -->", namesakes)

# 2.1
_teacher = "Владимир Вышкин"  # format: 'name surname'
teacher = get_teacher(_teacher, teachers_data)

if teacher:
    teachers_students = [get_full_name(student) for student in students_data
                         if student["school"] == teacher["school"] and student["class"] in teacher["class"]]
    print("2.1. Список всех учеников для учителя", _teacher, ": ", teachers_students)
else:
    print('2.1. Учитель %s не существует' % _teacher)

# 2.2
_student = "Александр Красный"
student = get_student(_student, students_data)

if student:
    students_teachers = [get_full_name(teacher) for teacher in teachers_data
                         if student["school"] == teacher["school"] and student["class"] in teacher["class"]]
    print("2.2. У ученика %s учителя %s" % (_student, students_teachers))
else:
    print('2.2. Ученик %s не существует' % _student)

# **************************lol*********хы******************************
import json
import os

DIR = 'data'


def save(data, file_name):
    """
    Сохраняем данные(data) в файл с именем file_name в формате JSON
    :param data: сохраняемые данные
    :type data: any type
    :param file_name: имя файла
    :type file_name: str
    """
    file = open(os.path.join(DIR, file_name), 'w', encoding="UTF-8")
    file.write(json.dumps(data, ensure_ascii=False))
    file.close()


students_data = json.load(open(os.path.join(DIR, 'Students.json'), 'r'))  # os.path.join - Вставляет нужный \ (Для исскуственного поддержания кросс-платформенности)
teachers_data = json.load(open(os.path.join(DIR, 'Teachers.json'), 'r'))  # константа - переменная которая не должна изменятся

student = {
    "name": "Петр",
    "middle_name": "Алексеевич",
    "surname": "Первый",
    "school": "67 школа",
    "class": "7 В",
    "birth_day": "06.06.1997"
}

students_data.append(student)

save(students_data, 'Students_new.json')


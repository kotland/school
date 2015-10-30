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
student_in_class = ['%s %s' % (student["name"], student["surname"]) for student in students_data
                    if student["class"] == class_room]
print("1.3. Список учеников из", class_room, " -->", student_in_class)

# Задача 1.4
schools = list(set(map(lambda student: student["school"], students_data)))
print("1.4. Список всех школ -->", schools)

# Задача 1.5
surnames = [student["surname"] for student in students_data]
same_surnames = [surname for surname in surnames if surnames.count(surname) > 1]
namesakes = ["%s %s" % (student["name"], student["surname"]) for student in students_data
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


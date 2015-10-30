import json
from utilities import location, clear, get_full_name, search
#
# def names(f={}):
# names=f['name']
# return names

def get_index(data, people_data, key):
    for student in data:
         if student[key] == people_data:
             return data.index(student)
    pass


def get_teacher(teacher_str, teachers_data):
    # Ищет и возвращает словарь с заданным учителя в списке

    name, surname = teacher_str.split(" ")
    for teacher in teachers_data:
        if teacher["name"] == name and teacher["surname"] == surname:
            return teacher


def get_student(student_str, students_data):
    # Ищет и возвращает словарь с заданным учеником в списке
    name, surname = student_str.split(" ")
    for student in students_data:
        if student["name"] == name and student["surname"] == surname:
            return student


def get_full_name(people):
    return "%s %s %s" % (people["name"], people["middle_name"], people["surname"])





# 1
data_student = json.load(open('Students.json'))
# print(data)
# students_names=[]
# for object in data_student:
# students_names.append(object["name"])
student_names = [student["name"] for student in data_student]
print(student_names)


# 2
data_teacher = json.load(open('Teachers.json'))
# for object in data_teacher:
# teachers_names.append(object["name"])
teachers_names = [teachers["name"] for teachers in data_teacher]
print(teachers_names)

# 3
class_room = "6 А"
students_in_class = ["%s %s" % (student["name"], student["surname"])
                     for student in data_student if student["class"] == class_room]
print(students_in_class)

# 4
student_school = list(set([student["school"] for student in data_student]))
# student_school_unique=[]
# for school in student_school:
#     if school in student_school_unique:
#         continue
#     else:
#         student_school_unique.append(school)

print(student_school)

# 5
student_surnames = [student["surname"] for student in data_student]
surnames = student_surnames.pop()
print(surnames)
# print(surname)

# 2.1
# class_teacher="Александр Черный"
# for teacher in data_teacher:
#     teacher_name_surname=class_teacher.split(' ')
#     if teacher["name"] == teacher_name_surname[0] and teacher["surname"] == teacher_name_surname[1]:
#         print("OK")
#     else:
#         print("No")
#     if
_teacher = "Владимир Вышкин"  # format: 'name surname'
teacher = get_teacher(_teacher, data_teacher)

if teacher:
    teachers_students = [get_full_name(student) for student in data_student
                         if student["school"] == teacher["school"] and student["class"] in teacher["class"]]
    print("2.1.", _teacher, ": ", teachers_students)
else:
    print('2.1. Учитель %s не существует' % _teacher)

# print(teacher_name_surname)

# if class_teacher in teachers_names_surnames:
# print(teachers_names)
# full_name= ["%s %s" % (student["name"], student["surname"])
#                  for student in data_student if student["class"]=="5 А "]
# full_name=[]
# 2.2
_student = "Александр Петрович"  # format: 'name surname'
student = get_student(_student, data_student)

if student:
    students_teachers = [get_full_name(teacher) for teacher in data_teacher
                         if student["school"] == teacher["school"] and student["class"] in teacher["class"]]
    print("2.2.", _student, ": ", students_teachers)
else:
    print('2.2. Ученик %s не существует' % _student)
# 3.1
DIR = '_data'
student = {
    "name": "Дмитрий",
    "middle_name": "Алексеевич",
    "surname": "Ким",
    "school": "12 гимназия",
    "class": "6 А",
    "birth_day": "05.11.1997"
}
data_student.append(student)
student = {
    "name": "Евгений",
    "middle_name": "Витальевич",
    "surname": "Быстрый",
    "school": "12 гимназия",
    "class": "7 В",
    "birth_day": "09.11.1997"
}
data_student.append(student)
print(data_student)
file = open('student_new.json', 'w', encoding="UTF-8")
file.write(json.dumps(data_student, ensure_ascii=False))
file.close()
# 3.2
teacher = {
    "name": "Владимир",
    "middle_name": "Сергеевич",
    "surname": "Юрченко",
    "school": "12 гимназия",
    "class": [
        "11 А",
        "6 Б",
        "6 Г",
        "9 В"
    ],
    "birth_day": "12.12.1982"
}
data_teacher.append(teacher)
teacher = {
    "name": "Иван",
    "middle_name": "Сергеевич",
    "surname": "Ермолов",
    "school": "12 гимназия",
    "class": [
        "10 А",
        "6 Б",
        "7 В"
    ],
    "birth_day": "24.12.1982"
}
data_teacher.append(teacher)
print(data_teacher)
file = open('teacher_new.json', 'w', encoding="UTF-8")
file.write(json.dumps(data_teacher, ensure_ascii=False))
file.close()
# 3,3



def get_index_name(name, data):
    for el in data:
        if el['name'] == name:
            return data.index(el)


new_class = '5 Г'
data_teacher[get_index_name('Иван', data_teacher)]['class'].append(new_class)
print('3.3', data_teacher)

# data_student.remove()

# 3.4



# get_index([{},{}], 'Иванов', 'surname')
#
#
# def get_index_name(name, data):
#     for student in data:
#          if student['name'] == name:
#              return data.index(student)
#
# def get_index_surname(surname,data):
#     for student in data:
#       if student['surname'] == surname:
#           return data.index(student)
#
# def get_index_middle_name(middle_name, data):
#     for student in data:
#         if student['middle_name'] == middle_name:
#             return data.index(student)



# print(get_index_surname('лоролдр', [{'surname': "Иванов"}, {'surname': "Петров"}]))
student_name='Артем'
student_surname='Валерьевич'
student_middle_name='Кузин'
if get_index(data_student,student_name,'name') == get_index(data_student,student_surname,'surnames') == get_index(data_student,student_middle_name,'middle_name'):
     print('1')
# print(get_index_middle_name(student_middle_name,data_student))

# d["key"]=val


import json
#
# def names(f={}):
#     names=f['name']
#     return names

# 1
data_student=json.load(open('Students.json'))
# print(data)
# students_names=[]
# for object in data_student:
#     students_names.append(object["name"])
student_names = [student["name"] for student in data_student]
print(student_names)


# 2
data_teacher=json.load(open('Teachers.json'))
# for object in data_teacher:
#     teachers_names.append(object["name"])
teachers_names = [teachers ["name"] for teachers in data_teacher]
print(teachers_names)

# 3
class_room="6 А"
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
surnames=student_surnames.pop()
print(surnames)
# print(surname)

# 2.1
class_teacher="Александр Черный"
for teacher in data_teacher:
    teacher_name_surname=class_teacher.split(' ')
    if teacher["name"] == teacher_name_surname[0] and teacher["surname"] == teacher_name_surname[1]:
        print("OK")
    else:
        print("No")
    if
# print(teacher_name_surname)

# if class_teacher in teachers_names_surnames:
# print(teachers_names)
    # full_name= ["%s %s" % (student["name"], student["surname"])
    #                  for student in data_student if student["class"]=="5 А "]
    # full_name=[]class_teacher[0]



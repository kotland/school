import json
import os
# from school import get_index
#5.1
with open('Students_id.json','r') as data_student:
    data_student = json.load(open('Students_id.json'))
# 4.2(1)
surname = "Кузин"
students_in_class = ["%s %s %s" % (student["name"], student["surname"], student["middle_name"])
                     for student in data_student if student["surname"] == surname]
print('4.2',students_in_class)
# 4.2(2)
id = 1
students_in_class = ["%s %s %s" % (student["name"], student["surname"], student["middle_name"])
                     for student in data_student if student["id"] == id]
print(students_in_class)
# 4.3
def get_people(people_data, **kwargs):
    for people in people_data:
        if people["name"] == kwargs['name'] or people["surname"] == kwargs['surname'] or people["middle_name"] ==kwargs["middle_name"] or people["class"] == kwargs['class'] or people["birth_day"] == kwargs["birth_day"]:
            # вставить пару условий с гет ...надо придумать как сделать так что б если одного усл нет то все все равно выполнялось data_student.get('surname', True)
            return people['id']

# student=[]

print(get_people(data_student, name='Иван', surname="Игоревич",birth_day= "12.07.1998", ))
#4.4
class_room = "6 А"
students_in_class = [(student["id"])
                     for student in data_student if student["class"] == class_room]
print(students_in_class)
#4.5

def get_index(data, people_data, key):
    for student in data:
         if student[key] == people_data:
             return data.index(student)
    pass


DIR = '_data'
#3
print(data_student[-1])
index=data_student[-1]['id']+1
#1
student = {
    "name": "Дмитрий",
    "middle_name": "Алексеевич",
    "surname": "Ким",
    "school": "12 гимназия",
    "class": "6 А",
    "birth_day": "05.11.1997"
}
#2
data_student.append(student)
#3


print('index =', index)
student["id"]=index
print(data_student)
file = open('student_new.json', 'w', encoding="UTF-8")
file.write(json.dumps(data_student, ensure_ascii=False))
file.close()
pass
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


students_data = json.load(open(os.path.join(DIR, 'Students.json'), 'r'))
teachers_data = json.load(open(os.path.join(DIR, 'Teachers.json'), 'r'))

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
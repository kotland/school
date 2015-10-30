import os
import json

DIR = 'data'

students_data = json.load(open(os.path.join(DIR, 'Students_id.json'), 'r'))


def search(peoples_list, **kwargs):
    return [people['id'] for people in peoples_list
            if (people['name'] == kwargs['name'] if kwargs.get('name') else True)
            and (people['surname'] == kwargs['surname'] if kwargs.get('surname') else True)
            and (people['class'] == kwargs['class_room'] or kwargs['class_room'] in people['class']
                 if kwargs.get('class_room') else True)]


# demo
print(search(students_data, name="Иван", class_room='5 А'))
print(search(students_data, name="Иван"))
print(search(students_data, name="Алексей"))

# 4.4
teachers_data = json.load(open(os.path.join(DIR, 'Teachers_id.json'), 'r'))
class_room = '7 В'
teachers_id = search(teachers_data, class_room=class_room)
print('id учитлей преподающих в %s: ' % class_room, teachers_id)
names = [teacher['name'] for teacher in teachers_data if teacher['id'] in teachers_id]
print('именя учитлей преподающих в %s: ' % class_room, names)
surnames = [teacher['surname'] for teacher in teachers_data if teacher['id'] in teachers_id]
print('фамилии учитлей преподающих в %s: ' % class_room, surnames)
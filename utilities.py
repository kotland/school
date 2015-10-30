import math
import os

location = lambda x: os.path.join(
    os.path.dirname(os.path.realpath(__file__)), x)


def clear():
    """
    Очищает консоль
    Не работает в консоли PyCharm'a
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def get_full_name(people):
    return "%s %s %s" % (people["name"], people["middle_name"], people["surname"])


def search(peoples_list, **kwargs):
    """
    :param peoples_list: список людей, в котором производится поиск. format: [{}, {}, ...]
    :param kwargs: набор именованных параметров поиска
    :return: Возвращает список людей(словари) с заданными именованными параметрами
    """
    return [people for people in peoples_list
            if (people['name'] == kwargs['name'] if kwargs.get('name') else True)
            and (people['surname'] == kwargs['surname'] if kwargs.get('surname') else True)
            and (people['class'] == kwargs['class_room'] or kwargs['class_room'] in people['class']
                 if kwargs.get('class_room') else True)]


def print_table(data, num_columns=1, num_sep=10, sort=False, dir_output='line'):
    """
    Выводит на печать указанную псследовательность в несколько столбиков
    :param data: последовательность
    :param num_columns: ко-во столбиков
    :param num_sep: кол-во пробелов между столбиками
    :param dir_output: направление вывода. line - по строкам / column - по столбикам
    """
    if sort:
        pass  # TODO: дописать сортировку

    n, line = 0, ""
    if dir_output == 'column':
        num_in_column = math.ceil(len(data)/num_columns)
        print(num_in_column)
        i = -1
        go = True
        try:
            while go:
                i += 1
                line = ''
                j = 0
                if i + 1 > num_in_column:
                    break
                while j < num_columns:
                    line += data[i + j * num_in_column] + " " * num_sep
                    j += 1

                print(line)
        except IndexError:
            if line:
                print(line)
    else:
        for el in data:
            n += 1
            if n <= num_columns:
                line += el + " " * num_sep
            else:
                print(line)
                n, line = 0, ""
        else:
            if line:
                print(line)


if __name__ == "__main__":
    print_table([
                    "5 А", "5 Б", "5 В", "5 Г",
                    "6 А", "6 Б", "6 В", "6 Г",
                    "7 А", "7 Б", "7 В", "7 Г",
                ], num_columns=3, dir_output='column')
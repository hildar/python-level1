__author__ = 'Хусаинов Ильдар Ришадович'

# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.


# Общую информацию выносим в Класс-предок (родитель)
class People:
    def __init__(self, name, surname, patronymic, birth_date):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic  # Отчество
        self.birth_date = birth_date

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_full_fio(self):
        return self.surname + ' ' + self.name + ' ' + self.patronymic

    def get_fio(self):
        return self.surname + ' {}.{}.'.format(self.name[0], self.patronymic[0])

    def set_name(self, new_name):
        self.name = new_name


class Parent(People):
    def __init__(self, name, surname, patronymic, birth_date, parent):
        # Явно вызываем конструктор родительского класса
        People.__init__(self, name, surname, patronymic, birth_date)
        self.parent = parent


# Сами классы наследуем
class Student(People):
    def __init__(self, name, surname, patronymic, birth_date, school, class_room, parent_mama, parent_dad):
        # Явно вызываем конструктор родительского класса
        People.__init__(self, name, surname, patronymic, birth_date)
        # Добавляем уникальные атрибуты
        self.school = school
        self.class_room = class_room
        self.parent_mama = parent_mama
        self.parent_dad = parent_dad

    # И уникальные методы
    def get_mama(self):
        return self.parent_mama

    def get_dad(self):
        return self.parent_dad

    def get_school(self):
        return self.school

    @property
    def get_class_room(self):
        return self.class_room

    def next_class(self):
        self.class_room = str(int(self.class_room.split()[0]) + 1) + ' ' + \
                          self.class_room.split()[1]


class Teacher(People):
    def __init__(self, name, surname, patronymic, birth_date, school, teach_classes, subject):
        People.__init__(self, name, surname, patronymic, birth_date)
        self.school = school
        self.teach_classes = teach_classes.split()
        self.subject = subject

    # Уникальный метод Учителя
    def get_teach_classes(self):
        return self.teach_classes

    def get_school(self):
        return self.school

    def get_subject(self):
        return self.subject


parent1_mama = Parent('Света', 'Пупкина', 'Вадимовна', '11.10.1982', 'Мама')
parent1_dad = Parent('Федор', 'Пупкин', 'Антонович', '01.07.1981', 'Папа')
parent2_mama = Parent('Юля', 'Шлёпкина', 'Альбертовна', '12.06.1989', 'Мама')
parent2_dad = Parent('Роберт', 'Шлёпкин', 'Артурович', '03.03.1985', 'Папа')
parent3_mama = Parent('Анна', 'Тапочкина', 'Альбертовна', '01.06.1983', 'Мама')
parent3_dad = Parent('Антон', 'Тапочкин', 'Андреевич', '06.03.1982', 'Папа')
parent4_mama = Parent('Анюта', 'Стакановна', 'Альбертовна', '01.06.1983', 'Мама')
parent4_dad = Parent('Анют', 'Стаканов', 'Андреевич', '06.03.1982', 'Папа')

student1 = Student('Вася', 'Пупкин', 'Федорович', '05.05.1991', 'Оксфорд', '4А',
                   parent1_mama.get_full_fio(), parent1_dad.get_full_fio())
student2 = Student('Алёша', 'Шлёпкин', 'Робертович', '06.06.1992', 'Оксфорд', '5Б',
                   parent1_mama.get_full_fio(), parent1_dad.get_full_fio())
student3 = Student('Алёша', 'Шлёпкин', 'Робертович', '06.06.1992', 'Оксфорд', '6В',
                   parent1_mama.get_full_fio(), parent1_dad.get_full_fio())
student4 = Student('Коля', 'Ушлёпкин', 'Сергеевич', '06.06.1993', 'Оксфорд', '5Б',
                   parent1_mama.get_full_fio(), parent1_dad.get_full_fio())

teacher1 = Teacher('Иван', 'Федоров', 'Александрович', '12.12.1952', 'Оксфорд', '4А 5Б 6В', 'Математика')
teacher2 = Teacher('Мария', 'Лопушкина', 'Ивановна', '22.02.1972', 'Оксфорд', '5Б 6В', 'Физика')
teacher3 = Teacher('Таисия', 'Семенова', 'Энштейновна', '22.03.1972', 'Оксфорд', '4А 5Б', 'Литература')


print('Учитель {} обучает {} классы предмету - {}'\
      ''.format(teacher2.get_fio(), teacher2.get_teach_classes(), teacher2.get_subject()))
print('Папа ученика {} - {}'.format(student1.get_full_name(), student1.get_dad()))
print('Ученик {} учится в {} классе'.format(student2.get_fio(), student2.get_class_room))


# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

# 1. Получить полный список всех классов школы
# Получаем через список учеников
def all_classes(*args):
    lst = [x for x in range(len(args))]
    for index, el in enumerate(args):
        lst[index] = el.get_class_room
    lst = list(set(lst))
    lst.sort()
    return lst


all_cls = all_classes(student1, student2, student3, student4)
print('Все классы в школе =', all_cls)
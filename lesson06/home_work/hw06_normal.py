# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# не совсем понимаю как используя парадигмы ООП реализовать школу
# ну чтож попробуем
#
# допустим это данные из базы данных школы: school_dict  ключ - id , значение - значение



class School:
    """
    инициализация класс школа
    устанавливает классы, предметы, учеников, учителей, классы -> предметы, учителя->предметы, ученики->классы,
    """
    def __init__(self, school):
        self.classes = school["classes"]
        self.courses = school["courses"]
        self.teachers = school["teachers"]
        self.students = school["students"]
        self.classes_courses = {}
        self.teachers_courses = {}
        self.students_classes = {}
        self.student_parents = {}
        if 'classes_courses' in school.keys():
            self.classes_courses = school["classes_courses"]
        if 'teachers_courses' in school.keys():
            self.teachers_courses = school["teachers_courses"]
        if 'students_classes' in school.keys():
            self.students_classes = school["students_classes"]
        if 'student_parents' in school.keys():
            self.student_parents = school["student_parents"]


    def get_classes(self):
        print("классы школы ", self.classes)

    """
    :param classes_courses dict вида {id_класса : [id_предмета, id_предмета]}
    """
    def set_classes_courses(self, classes_courses):
        for key, value in classes_courses.items():
            if key in self.classes.keys() and len([kc for kc in value if kc in self.classes.keys()]) > 0:
                self.classes_courses.update(map(key, value))
            else:
                print("Класса ({}) или предмета {} с такими id в школе не существует".format(key, value))

    """
    :param classes_courses dict вида {id_преподавателя : id_предмета}
    """
    def set_teachers_courses(self, teachers_courses):
        for key, value in teachers_courses:
            if key in self.teachers.keys() and value in self.courses.keys() and key not in self.teachers_courses.keys():
                self.teachers_courses.update(map(key, value))

    """
      :param classes_courses dict вида {id_студента : id_класса}
    """
    def set_students_classes(self, students_classes):
        for key, value in students_classes.items():
            if key in self.students.keys() and value in self.classes.keys():
                self.students_classes.update(map(key, value))


class Student(School):
    def __init__(self, school):
        School.__init__(self, school)

    """
      Приватный метод
      Возвращает id учителя по Имени
      """

    def __get_teacher_by_name(self, teach):
        for idx, class_name in self.students.items():
            if class_name in teach:
                return idx
        print("Ученик {} не найден".format(teach))
        return False

    """
    Приватный метод
    Возвращает id ученика по Имени
    """
    def __get_student_by_name(self, stud):
        for idx,class_name in self.students.items():
            if class_name in stud:
                return idx
        print("Ученик {} не найден".format(stud))
        return False

    """
    Приватный метод
    Возвращает id класса по наименованию
    """
    def __get_class_by_name(self, class_):
        for idx,class_name in self.classes.items():
            if class_name == class_:
                return idx
        print("Класс {} не найден".format(class_))
        return False

    def get_students_in_class(self, class_):
        if type(class_) == str:
            class_ = self.__get_class_by_name(class_)
        if not class_:
            return
        print("Список учеников {} класса: ".format(self.classes[class_]))
        for idx, val in self.students_classes.items():
            if val == class_:
                print(self.students[idx])

    def get_student_info(self, stud):
        if type(stud) == str:
            stud = self.__get_student_by_name(stud)
        if not stud:
            return
        class_ = self.students_classes[stud]
        print("Ученик {} учится в {}".format(self.students[stud], self.classes[class_]))
        self.get_class_teachers(class_)

    def __get_teacher_course(self, course_id):
        for idx, val in self.teachers_courses.items():
            if val == course_id:
                return idx
        return False

    def get_class_teachers(self, class_, mode='all'):
        if type(class_) == str:
            class_ = self.__get_class_by_name(class_)
        if not class_:
            return
        if mode == 'all':
            print("Cписок предметов и учителей в классе {}:".format(self.classes[class_]))
        else:
            print("Cписок учителей в классе {}:".format(self.classes[class_]))
        for idx, val in self.classes_courses.items():
            if idx == class_:
                for course_id in val:
                    teach_id = self.__get_teacher_course(course_id)
                    if not teach_id:
                        return
                    if mode == 'all':
                        print("Предмет: {} Преподаватель: {}".format(self.courses[course_id], self.teachers[teach_id]))
                    else:
                        print("Преподаватель: {}".format(self.teachers[teach_id]))

    def get_student_parents(self, stud):
        if type(stud) == str:
            stud = self.__get_student_by_name(stud)
        if not stud:
            return
        print('Родители ученика {}: \n Мать: {} \n Отец: {}'.format(self.students[stud], self.student_parents[stud]['mom'], self.student_parents[stud]['dad']))


school_dict = {
    'classes': {
        1: '8а',
        2: '9б'
    },
    'courses': {
        1: 'Алгебра',
        2: 'Физика',
        3: 'Геометрия',
        4: 'История'
    },
    'teachers': {
        1: 'Борисов А.В',
        2: 'Сидоренко С.С',
        3: 'Филатов П.Е.',
        4: 'Бельчинский К.А.'
    },
    'students': {
        1: 'Петров А.Г',
        2: 'Сидоров С.С',
        3: 'Иванов П.Е.',
        4: 'Соколов К.А.',
        5: 'Журавлев К.В.',
        6: 'Даньшин А.В.'
    },
    'classes_courses': {
        1: [1, 3, 4],
        2: [1, 2, 3, 4]
    },
    'teachers_courses': {
        1: 4,
        2: 3,
        3: 1,
        4: 2,
    },
    'students_classes': {
        1: 1,
        2: 1,
        3: 1,
        4: 2,
        5: 2,
        6: 2,
    },
    'student_parents': {
            1: {"mom": "Петрова В.В", "dad": "Петров Г.Х"},
            2: {"mom": "Сидорова А.Н", "dad": "Сидоров С.Н"},
            3: {"mom": "Иванова А.К","dad": "Иванов П.Ф"},
            4: {"mom": "Соколова Д.Х","dad": "Соколов К.П"},
            5: {"mom": "Журавлева Т.Г", "dad": "Журавлев В.М"},
            6: {"mom": "Даньшина Л.З", "dad": "Даньшин В.П"},

    }
}
student = Student(school_dict)
student.get_classes()
student.get_students_in_class('8а')
student.get_student_info('Журавлев К.В.')
student.get_student_parents('Журавлев К.В.')
student.get_class_teachers('9б', 'teachers')

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы School-->get_classes()
# 2. Получить список всех учеников в указанном классе Student-->get_students_in_class("id или наименование класса")
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика  Student-->get_student_info('Журавлев К.В.')
#  (Ученик --> Класс --> Учителя --> Предметы) - не совсем понятно что это, выведу всю инфу
# 4. Узнать ФИО родителей указанного ученика Student-->get_student_parents('ФИО')
# 5. Получить список всех Учителей, преподающих в указанном классе Student-->get_class_teachers('ФИО или id', 'teachers')




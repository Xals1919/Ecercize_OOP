class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress \
                and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average(self):
        count = 0
        quantity = 0
        for rating in self.grades.values():
            for rating_1 in rating:
                count += rating_1
                quantity += 1
        return round((count / quantity), 1)

    def __str__(self):
        res = f'Имя = {self.name}\nФамилия = {self.surname}\nСредняя оценка за лекции: {self._average()}' \
              f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}' \
              f'\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Нет студентов')
            return
        return self._average() < other._average()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average(self):
        count = 0
        quantity = 0
        for rating in self.grades.values():
            for rating_1 in rating:
                count += rating_1
                quantity += 1
        return round((count / quantity), 1)

    def __str__(self):
        res = f'Имя = {self.name}\nФамилия = {self.surname}\nСредняя оценка за лекции: {self._average()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Нет лекторов')
            return
        return self._average() < other._average()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя = {self.name}\nФамилия = {self.surname}'
        return res


# Студенты
some_student_1 = Student('Roy', 'Eman', 'your_gender')
some_student_1.courses_in_progress += ['Python', 'Git']
some_student_1.finished_courses += ['Введение в программирование']
some_student_2 = Student('Arnold', 'Ewans', 'your_gender')
some_student_2.courses_in_progress += ['Python', 'Git']
some_student_2.finished_courses += ['Введение в программирование']

# Менторы
cool_mentor = Mentor('Irina', 'Masker')
cool_mentor.courses_attached += ['Python']

# Лекторы
some_lecturer_1 = Lecturer('Brain', 'Diz')
some_lecturer_1.courses_attached += ['Python']
some_lecturer_2 = Lecturer('Rou', 'Vinz')
some_lecturer_2.courses_attached += ['Python']

# Эксперты
some_reviewer = Reviewer('Jon', 'Yoke')
some_reviewer.courses_attached += ['Python', 'Git']

# Оценки студентов
some_reviewer.rate_hw(some_student_1, 'Python', 10)
some_reviewer.rate_hw(some_student_1, 'Git', 7)
some_reviewer.rate_hw(some_student_1, 'Python', 6)
some_reviewer.rate_hw(some_student_2, 'Git', 5)
some_reviewer.rate_hw(some_student_2, 'Python', 9)
some_reviewer.rate_hw(some_student_2, 'Python', 6)

# Оценки лекторов
some_student_1.rate_hw(some_lecturer_1, 'Python', 9)
some_student_1.rate_hw(some_lecturer_1, 'Python', 6)
some_student_1.rate_hw(some_lecturer_1, 'Git', 4)
some_student_2.rate_hw(some_lecturer_2, 'Python', 10)
some_student_2.rate_hw(some_lecturer_2, 'Python', 7)
some_student_2.rate_hw(some_lecturer_2, 'Git', 4)

# print(some_student_1.grades)
# print(some_student_2.grades)
# print(some_reviewer)
# print(some_student_1)
# print(some_student_2)
# print(some_student_1 > some_student_2)
# print(some_lecturer_1)
# print(some_lecturer_2)
# print(some_lecturer_1 < some_lecturer_2)

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
student_1 = Student('Roy', 'Eman', 'your_gender')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Arnold', 'Ewan', 'your_gender')
student_2.courses_in_progress += ['Python', 'Git']
student_2.finished_courses += ['Введение в программирование']

# Менторы
mentor_1 = Mentor('Irina', 'Masker')
mentor_1.courses_attached += ['Python', 'Git']
mentor_2 = Mentor('German', 'Poker')
mentor_2.courses_attached += ['Введение в программирование']

# Лекторы
lecturer_1 = Lecturer('Brain', 'Diz')
lecturer_1.courses_attached += ['Python', 'Git']
lecturer_2 = Lecturer('Rou', 'Vinz')
lecturer_2.courses_attached += ['Python', 'Введение в программирование', 'Git']

# Эксперты
reviewer_1 = Reviewer('Jon', 'Yoke')
reviewer_1.courses_attached += ['Python', 'Git']
reviewer_2 = Reviewer('Vanesa', 'Karlo')
reviewer_2.courses_attached += ['Python', 'Введение в программирование', 'Git']

# Методы
# Оценки студентов
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Git', 7)
reviewer_1.rate_hw(student_1, 'Python', 6)
reviewer_2.rate_hw(student_2, 'Git', 5)
reviewer_2.rate_hw(student_2, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Python', 6)

# Оценки лекторов
student_1.rate_hw(lecturer_1, 'Python', 9)
student_1.rate_hw(lecturer_1, 'Python', 6)
student_1.rate_hw(lecturer_1, 'Git', 4)
student_2.rate_hw(lecturer_2, 'Python', 10)
student_2.rate_hw(lecturer_2, 'Python', 7)
student_2.rate_hw(lecturer_2, 'Git', 4)

print(reviewer_1)
print(reviewer_2)

print(student_1)
print(student_2)
print(student_1 > student_2)

print(lecturer_1)
print(lecturer_2)
print(lecturer_1 > lecturer_2)

students = [student_1, student_2]
lecturers = [lecturer_1, lecturer_2]
course = 'Python'


def average_rating_student(student, courses):
    for person in student:
        if courses in person.courses_in_progress:
            count = 0
            quantity = 0
            for rating in person.grades.values():
                for rating_1 in rating:
                    count += rating_1
                    quantity += 1
            print(f'Студент {person.name} на курсе {courses} имеет средний бал {round((count / quantity), 1)}')


def average_rating_lecturers(lecturer, courses):
    for person in lecturer:
        if courses in person.courses_attached:
            count = 0
            quantity = 0
            for rating in person.grades.values():
                for rating_1 in rating:
                    count += rating_1
                    quantity += 1
            print(f'Лектор {person.name} на курсе {courses} имеет средний бал {round((count / quantity), 1)}')


average_rating_student(students, course)
average_rating_lecturers(lecturers, course)


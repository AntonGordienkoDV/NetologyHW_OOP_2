class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in (self.finished_courses + self.courses_in_progress) \
                and course in lecturer.courses_attached:
            lecturer.grades[course] = lecturer.grades.setdefault(course, []) + [grade]
        else:
            return 'Ошибка'

    def _mean_grade(self):
        mean_gr = 0
        grade_counter = 0
        for _grades in self.grades.values():
            mean_gr += sum(_grades)
            grade_counter += len(_grades)
        else:
            if mean_gr:
                mean_gr /= grade_counter
        return mean_gr

    def __str__(self):
        res = f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {self._mean_grade():.2f}
Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
Завершенные курсы: {', '.join(self.finished_courses)}'''
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return super().__str__() + f'\nСредняя оценка за лекции: {self._mean_grade():.2f}'

    def _mean_grade(self):
        mean_gr = 0
        grade_counter = 0
        for _grades in self.grades.values():
            mean_gr += sum(_grades)
            grade_counter += len(_grades)
        else:
            if mean_gr:
                mean_gr /= grade_counter
        return mean_gr

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print(f'Not a Lecturer')
            return
        return self._mean_grade() < other._mean_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            student.grades[course] = student.grades.setdefault(course, []) + [grade]
        else:
            return 'Ошибка'


def main():
    st1 = Student('Greg', 'Mouse', 'Male')
    st1.courses_in_progress += ['GIT', 'SQL']
    st1.finished_courses += ['Python']
    lc1 = Lecturer('John', 'Daw')
    lc1.courses_attached += ['GIT', 'Python']
    rv1 = Reviewer('Jane', 'Dawson')
    rv1.courses_attached += ['GIT', 'Python', 'SQL']
    rv1.rate_hw(st1, 'GIT', 10)
    rv1.rate_hw(st1, 'GIT', 9)
    rv1.rate_hw(st1, 'GIT', 9)
    rv1.rate_hw(st1, 'SQL', 8)
    lc2 = Lecturer('Johan', 'Izralyevich')
    lc2.courses_attached += ['GIT', 'SQL']
    st1.rate_lecture(lc1, 'GIT', 9)
    st1.rate_lecture(lc1, 'GIT', 10)
    st1.rate_lecture(lc1, 'Python', 5)
    st1.rate_lecture(lc2, 'GIT', 9)
    st1.rate_lecture(lc2, 'SQL', 9)
    st1.rate_lecture(lc2, 'SQL', 10)
    print(lc1)
    print(lc2)
    print(lc1 < lc2)
    print(lc1 > lc2)
    pass


if __name__ == '__main__':
    main()

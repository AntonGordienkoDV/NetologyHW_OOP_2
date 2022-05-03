class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, *grade):
        if isinstance(lecturer, Lecturer) and course in (self.finished_courses + self.courses_in_progress) \
                and course in lecturer.courses_attached:
            lecturer.grades[course] = lecturer.grades.setdefault(course, []) + [*grade]
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

    def __lt__(self, other):
        if not isinstance(other, Student):
            print(f'Not a Student')
            return
        return self._mean_grade() < other._mean_grade()


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
    def rate_hw(self, student, course, *grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            student.grades[course] = student.grades.setdefault(course, []) + [*grade]
        else:
            return 'Ошибка'


def main():
    # Creating Student Objects
    st1 = Student('Anton', 'Gordienko', 'Male')
    st2 = Student('Iola', 'Orfey', 'Female')
    st1.courses_in_progress += ['Python', 'SQL']
    st1.finished_courses += ['GIT']
    st2.courses_in_progress += ['Python', 'GIT']
    # Creating Reviewer Objects
    rv1 = Reviewer('John', 'Daw')
    rv1.courses_attached += ['Python']
    rv2 = Reviewer('Jane', 'Daw')
    rv2.courses_attached += ['GIT', 'SQL']
    # Creating Lecturer Objects
    lc1 = Lecturer('Guido', 'van Rossum')
    lc1.courses_attached += ['Python', 'SQL']
    lc2 = Lecturer('Linus', 'Torvalds')
    lc2.courses_attached += ['GIT']
    # Rate Lecturers
    st1.rate_lecture(lc1, 'Python', 10, 10, 8)
    st1.rate_lecture(lc1, 'SQL', 5, 9)
    st1.rate_lecture(lc2, 'GIT', 10, 9, 8, 7)
    st2.rate_lecture(lc1, 'Python', 10, 10, 8)
    st2.rate_lecture(lc2, 'GIT', 10, 8, 8, 9)
    # Rate Students
    rv1.rate_hw(st1, 'Python', 9, 8, 10)
    rv1.rate_hw(st1, 'Python', 5)
    rv1.rate_hw(st2, 'Python', 10, 8, 10)
    rv2.rate_hw(st2, 'GIT', 7, 8, 8)
    rv2.rate_hw(st1, 'SQL', 9)
    rv2.rate_hw(st1, 'GIT', 10, 7, 5)  # Эта команда не сработает, так как GIT у первого студента в списке завершенных
    st1.grades['GIT'] = [10, 7, 5]  # Добавим эти оценки вручную
    # Check print function
    print(st1, st2, rv1, rv2, lc1, lc2, sep='\n\n')
    # Check comparison function
    print(st1 < st2, st1 > st2, lc1 < lc2, lc1 > lc2, sep='\n')
    pass


if __name__ == '__main__':
    main()

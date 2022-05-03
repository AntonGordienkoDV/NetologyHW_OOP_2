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


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


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
    rv1.courses_attached += ['GIT', 'Python']
    rv1.rate_hw(st1, 'GIT', 10)
    rv1.rate_hw(st1, 'GIT', 8)
    rv1.rate_hw(st1, 'GIT', 9)
    st1.rate_lecture(lc1, 'GIT', 10)
    pass


if __name__ == '__main__':
    main()

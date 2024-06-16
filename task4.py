class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average(self):
        total_grades = []
        for grades in self.grades.values():
            total_grades.extend(grades)
        if total_grades:
            return sum(total_grades) / len(total_grades)

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.average()}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}")

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Error")
            return
        return self.avg_rate() < other.avg_rate()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average(self):
        total_grades = []
        for grades in self.grades.values():
            total_grades.extend(grades)
        if total_grades:
            return sum(total_grades) / len(total_grades)

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.average()}")

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Error")
            return
        return self.avg_rate() < other.avg_rate()


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
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}")


student1 = Student('Алексей', 'Иванов', 'М')
student2 = Student('Мария', 'Смирнова', 'Ж')

lecturer1 = Lecturer('Александр', 'Белов')
lecturer2 = Lecturer('Елена', 'Новикова')

reviewer1 = Reviewer('Иван', 'Петров')
reviewer2 = Reviewer('Анна', 'Кузнецова')

student1.courses_in_progress += ['Python', 'Java']
student2.courses_in_progress += ['Python', 'Delphi']

student1.finished_courses += ['C++']
student2.finished_courses += ['HTML']

lecturer1.courses_attached += ['Python', 'Java']
lecturer2.courses_attached += ['Python', 'Delphi']

reviewer1.courses_attached += ['Python', 'Java']
reviewer2.courses_attached += ['Python', 'Delphi']

reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student1, 'Java', 7)
reviewer2.rate_hw(student2, 'Python', 9)
reviewer2.rate_hw(student2, 'Delphi', 10)

student1.rate_lecturer(lecturer1, 'Python', 9)
student1.rate_lecturer(lecturer1, 'Java', 8)
student2.rate_lecturer(lecturer2, 'Python', 10)
student2.rate_lecturer(lecturer2, 'Delphi', 9)

print(f"{student1}\n\n"
      f"{student2}\n\n"
      f"{lecturer1}\n\n"
      f"{lecturer2}\n\n"
      f"{reviewer1}\n\n"
      f"{reviewer2}")

def average_grade_students(students, course):
    total_grades = []
    for student in students:
        if course in student.grades:
            total_grades.extend(student.grades[course])
    if total_grades:
        return sum(total_grades) / len(total_grades)

def average_grade_lecturers(lecturers, course):
    total_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades.extend(lecturer.grades[course])
    if total_grades:
        return sum(total_grades) / len(total_grades)

students = [student1, student2]
lecturers = [lecturer1, lecturer2]
print(f"Средняя оценка по 'Python': {average_grade_students(students, 'Python')}")
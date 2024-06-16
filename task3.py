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


# Student
best_student = Student('Алексей', 'Иванов', 'М')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Python']
best_student.courses_in_progress += ['Java']
best_student.finished_courses += ['Java']
best_student.courses_in_progress += ['Delphi']
best_student.finished_courses += ['Delphi']

# Reviewer
cool_reviewer = Reviewer('Иван', 'Петров')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Java']
cool_reviewer.courses_attached += ['Delphi']

cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(best_student, 'Java', 4)
cool_reviewer.rate_hw(best_student, 'Delphi', 9)

# Lecturer
cool_lecturer = Lecturer('Александр', 'Белов')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Java']
cool_lecturer.courses_attached += ['Delphi']

best_student.rate_lecturer(cool_lecturer, 'Python', 9)
best_student.rate_lecturer(cool_lecturer, 'Java', 8)
best_student.rate_lecturer(cool_lecturer, 'Delphi', 10)

print(f"{best_student}\n\n"
      f"{cool_lecturer}\n\n"
      f"{cool_reviewer}")

class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        if self.is_married:
            married = 'женат(замужем)'
        else:
            married = 'не женат(незамужем'
        print(f'имя: {self.fullname}, age: {self.age}, is_marrie: {married}')


class Student(Person):
    def __init__(self, fullname, age, is_merried, marks):
        super().__init__(fullname, age, is_merried,)
        self.marks = marks

    def average_marks(self):
        if not self.marks:
            return 0

        return sum(self.marks.values()) / len(self.marks)

class Teacher(Person):
    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def base_salare(self):
        base_salare = 35000
        bonus = 0
        percentage = self.experience / 3
        if self.experience >= 3:
            bonus = (0.05 * percentage) * base_salare
            return f'зарплата учителя {self.fullname} составляет', base_salare + bonus


teacher = Teacher("Виктор", 34, True, 12)
teacher.introduce_myself()
print(f'зарплата{teacher.base_salare()}')


def create_students():
    students = [
        Student('Алим', 17, False, {"математика": 5, "История": 5, "физика": 4}),
        Student("Ислам", 16, False, {"математика": 4, "История": 4, "физика": 4}),
        Student("Селим", 16, False, {"математика": 5, "История": 3, "физика": 4})
    ]

    return students

students = create_students()
for student in students:
    student.introduce_myself()
    print(f"оценки:{student.marks}\n"
          f"Средняя оценка: {student.average_marks()}\n")

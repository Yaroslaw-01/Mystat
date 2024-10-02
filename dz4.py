class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0


class StudentGroup:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def best_student(self):
        if not self.students:
            return None
        return max(self.students, key=lambda student: student.average_grade())


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name}.")

    def __len__(self):
        return self.age


class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount

    def get_balance(self):
        return self.balance


student1 = Student("Alice", [90, 85, 92])
student2 = Student("Bob", [78, 82, 88])

group = StudentGroup()
group.add_student(student1)
group.add_student(student2)

best_student = group.best_student()
if best_student:
    print(f"Best student: {best_student.name} with average grade: {best_student.average_grade()}")

person = Person("John", 30)
person.say_hello()
print(len(person))

account = BankAccount("123456789")
account.deposit(500)
account.withdraw(200)
print(f"Current balance: {account.get_balance()}")
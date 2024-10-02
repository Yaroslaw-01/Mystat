class Animal:
    def __init__(self, name, age, kind):
        self.name = name
        self.age = age
        self.kind = kind

    def sound(self):
        raise NotImplementedError

    def info(self):
        return f"{self.name}, {self.kind}, {self.age}"


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, "Dog")
        self.breed = breed

    def sound(self):
        return "Woof-woof"

    def info(self):
        return f"{self.name}, {self.breed}, {self.age}"


class Cat(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, "Cat")
        self.breed = breed

    def sound(self):
        return "Meow"

    def info(self):
        return f"{self.name}, {self.breed}, {self.age}"


dog = Dog("Barsik", 3, "Korgi")
cat = Cat("Murka", 2, "Siam")

print(dog.info())
print(dog.sound())

print(cat.info())
print(cat.sound())
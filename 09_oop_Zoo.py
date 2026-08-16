class Animal:
    def __init__(self, name, sound):
        if not name or not sound:
            raise ValueError("❌ Name and sound cannot be empty!")
        self.name = name
        self.sound = sound

    def make_sound(self):
        return f"{self.name} says: {self.sound}"


class Dog(Animal):
    def __init__(self):
        super().__init__("Dog", "HAP HAP")


class Cat(Animal):
    def __init__(self):
        super().__init__("Cat", "MIOOOOW")


class Cow(Animal):
    def __init__(self):
        super().__init__("Cow", "MOWWW")


class Bird(Animal):
    def __init__(self):
        super().__init__("Bird", "CHICK CHICK")


class Elephant(Animal):
    def __init__(self):
        super().__init__("Elephant", "TRUMPET")




animals = [Dog(), Cat(), Cow(), Bird(), Elephant()]

for animal in animals:
    print(animal.make_sound())


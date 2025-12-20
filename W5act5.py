# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"Animal Name: {self.name}")


# Level 1 subclasses
class Mammal(Animal):
    def __init__(self, name, feature):
        super().__init__(name)
        self.feature = feature


class Bird(Animal):
    def __init__(self, name, feature):
        super().__init__(name)
        self.feature = feature


class Fish(Animal):
    def __init__(self, name, feature):
        super().__init__(name)
        self.feature = feature


# Level 2 subclasses
class Dog(Mammal):
    def walk(self):
        print(f"{self.name} can walk")


class Cat(Mammal):
    def walk(self):
        print(f"{self.name} can walk")


class Eagle(Bird):
    def fly(self):
        print(f"{self.name} can fly")


class Penguin(Bird):
    def swim(self):
        print(f"{self.name} can swim")


class Salmon(Fish):
    def swim(self):
        print(f"{self.name} can swim")


class Shark(Fish):
    def swim(self):
        print(f"{self.name} can swim")


# Main program
if __name__ == "__main__":
    dog = Dog("Dog", "Warm-blooded")
    cat = Cat("Cat", "Fur")
    eagle = Eagle("Eagle", "Wings")
    penguin = Penguin("Penguin", "Flippers")
    salmon = Salmon("Salmon", "Gills")
    shark = Shark("Shark", "Sharp teeth")

    dog.walk()
    cat.walk()

    eagle.fly()
    penguin.swim()

    salmon.swim()
    shark.swim()

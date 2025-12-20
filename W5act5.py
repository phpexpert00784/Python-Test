# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        # Common method for all animals
        print(f"I am an animal named {self.name}")


# Child class of Animal
class Mammal(Animal):
    def __init__(self, name, feature):
        super().__init__(name)
        self.feature = feature

    def show_feature(self):
        print(f"Mammal feature: {self.feature}")


# Child class of Animal
class Bird(Animal):
    def __init__(self, name, feature):
        super().__init__(name)
        self.feature = feature

    def show_feature(self):
        print(f"Bird feature: {self.feature}")


# Child class of Animal
class Fish(Animal):
    def __init__(self, name, feature):
        super().__init__(name)
        self.feature = feature

    def show_feature(self):
        print(f"Fish feature: {self.feature}")


# ----- Mammal children -----

class Dog(Mammal):
    # Function overriding:
    # walk() is specific to Dog
    def walk(self):
        print(f"{self.name} the dog walks on four legs")


class Cat(Mammal):
    # Function overriding:
    # walk() is specific to Cat
    def walk(self):
        print(f"{self.name} the cat walks silently")


# ----- Bird children -----

class Eagle(Bird):
    # Function overriding:
    # fly() is specific to Eagle
    def fly(self):
        print(f"{self.name} the eagle flies very high")


class Penguin(Bird):
    # Function overriding:
    # Penguins cannot fly, so swim() is implemented instead
    def swim(self):
        print(f"{self.name} the penguin swims in cold water")


# ----- Fish children -----

class Salmon(Fish):
    # Function overriding:
    # swim() behavior for Salmon
    def swim(self):
        print(f"{self.name} the salmon swims upstream")


class Shark(Fish):
    # Function overriding:
    # swim() behavior for Shark
    def swim(self):
        print(f"{self.name} the shark swims fast and hunts")


# ----------- Testing the project -----------

dog = Dog("Buddy", "Warm-blooded")
cat = Cat("Kitty", "Warm-blooded")

eagle = Eagle("Rocky", "Feathers")
penguin = Penguin("Pingo", "Flightless bird")

salmon = Salmon("Sal", "Cold-blooded")
shark = Shark("Jaws", "Predator")

dog.walk()
cat.walk()

eagle.fly()
penguin.swim()

salmon.swim()
shark.swim()

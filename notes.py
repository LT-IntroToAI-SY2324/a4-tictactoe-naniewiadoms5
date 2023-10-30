# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

class Dog:
    # functions that start with __ are not intended to be called directly
    def __init__(self, n = "", fc = "", a = 0, ff = ""):
        """Creates an instance of the dog class and sets attributes"""
        self.name = n
        self.fur_color = fc
        self.age = a
        self.favorite_food = ff
        self.fetch_count = 0

    def __str__(self) -> str:
        """Return a string representation of a dog"""
        s = "Dog's name is " + self.name + "\n"
        s+= "and age is " + str(self.age) + "\n"
        s+= "and fur color is " + self.fur_color + "\n"
        s+= "they have played fetch " + str(self.fetch_count) + " times \n"
        return s
    
    def play_fetch(self, num_times):
        self.fetch_count += num_times

    def paint_dog(self, color):
        self.fur_color = color

    myDog = Dog("Logan", "Black", 7, "Salmon")
    chrisDog = Dog("Luna", "Black and White", 6, "Tortillas")

    print(myDog)
    print(chrisDog)

    myDog.play_fetch(20)
    chrisDog.play_fetch(3)

    print(myDog)
    print(f"{chrisDog.name} has played fetch {chrisDog.fetch_count} times")

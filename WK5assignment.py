'''
class animal:
    def __init__(self):
        pass

class dog(animal):                          # dog class inherits from animal class
    def speak(self):
        return "woof!"
    def muve(self):
        return "runs on all fours"

class cat(animal):                           # cat class inherits from animal class
    def speak(self):
        return "meow!"
    def muve(self):
        return "walks"

class bird(animal):                            # bird class inherits from animal class
    def speak(self):
        return "chirp!"
    def muve(self):
        return "flies"

myAnimal = dog()
print(myAnimal.speak())
print(myAnimal.muve())

myAnimal = cat()
print(myAnimal.speak())
print(myAnimal.muve())

myAnimal = bird()
print(myAnimal.speak())
print(myAnimal.muve())

for animal in [dog(), cat(), bird()]:
    print(animal.speak())
    print(animal.muve())
'''

    # Updated classes to use constructors with unique values
class animal:
    def __init__(self):
        pass

class dog(animal):                          # dog class inherits from animal class
    def __init__(self):
        pass
    def speak(self):
        return "woof!"
    def muve(self):
        return "runs on all fours"

class cat(animal):                           # cat class inherits from animal class
    def __init__(self):
        pass
    def speak(self):
        return "meow!"
    def muve(self):
        return "walks"

class bird(animal):                            # bird class inherits from animal class
    def __init__(self):
        pass
    def speak(self):
        return "chirp!"
    def muve(self):
        return "flies"

myAnimal = dog()
print(myAnimal.speak())
print(myAnimal.muve())

myAnimal = cat()
print(myAnimal.speak())
print(myAnimal.muve())

myAnimal = bird()
print(myAnimal.speak())
print(myAnimal.muve())
'''
for animal in [dog("Buddy"), cat("Whiskers"), bird("Tweety")]:
    print(animal.speak())
    print(animal.muve())
'''
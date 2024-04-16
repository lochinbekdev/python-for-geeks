class Person:
    species = "Home species"

    def __init__(self, name,age):
        self.name = name
        self.age = age


person1=Person('Alice',20)
person2=Person('John',30)

print(person1.name)
print(person1.age)
print(Person.species)   
        


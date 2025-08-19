# Example of class
class TestClass:
    def __init__(self,nm):
        self.name = nm
        print(self.name)

    def test(self,age):
        self.age= age
        print(f'test : {self.name} and age is {self.age}')
        return True


obj = TestClass('KAAL')  
print(obj.test(34))

# Built in Class Functions : getattr,setattr,delattr,hasattr
print(f"example of getattr: {getattr(obj,'age')}")
setattr(obj,'age',56) # setattr() does not return the value it sets
print(f"example of setattr: {getattr(obj,'age')}")
print(f"dispaly full object: {obj.__dict__}")


# example of build-in class attribute
print(f"==========================example of build-in class attribute===========================")
class Person:
    """This is a Person class"""
    species = "Homo sapiens"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def change_species(cls):
        cls.species = "Homo ergaster"
        return cls.species
        
    def hello(self):
        pass

p = Person("Alice", 30)

# Built-in class attributes
print(Person.__doc__)     # "This is a Person class"
print(Person.__name__)    # "Person"
print(Person.__module__)  # "__main__" (since we ran directly)
print(Person.__bases__)   # (<class 'object'>,)
print(Person.__dict__)    # Shows attributes & methods in dict form


print(Person.species) # class variable
print(Person.change_species()) #modifiy the class variable using class method


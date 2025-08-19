class Parent:
    def __init__(self,sal,exp):
        self.sal = sal
        self.exp = exp
    def display(self,name):
        return f"The employee Name is: {name} and his Experince is: {self.exp} and Salary is: {self.sal}"

class Child(Parent):
    age = 34
    # def __init__(self, sal, exp):
    #     super().__init__(sal, exp)


obj = Child(100000,10)
print(f'display the name: {obj.display('Abhijit')}')
print(f'display the age: {obj.age}')


class Child2(Parent):
    age = 27

obj2 = Child2(1200000,20)
print(f'display the name: {obj2.display('Abhijit')}')
print(f'display the age: {obj2.age}')
class Employee:
    def __init__(self,name,sal):
        self.name = name
        self.sal = sal
    
    def show(self):
        print(f"Employee name is {self.name} and his salary is {self.sal}")
    

emp_obj = Employee('Raju',100)
emp_obj.show()

# change the salary using static method

class Emp_modify:
    @staticmethod
    def modify_sal(obj):
        obj.sal = obj.sal + 400
        obj.show()


modify_obj = Emp_modify()
modify_obj.modify_sal(emp_obj)

# Another Example

class Bank:
    __rate = 8.5   # private class variable

    @staticmethod
    def calculate_interest(principal, years):
        return (principal * Bank.__rate * years) / 100


print(Bank.calculate_interest(10000, 2)) 
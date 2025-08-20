import time
class Team:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    # def fullname(self):
    #     fullname = self.fname + self.lname
    #     return fullname

    # def mail(self,name):
    #     self.fname,self.lname = name.split()
    #     return f"email id is: {self.fname.lower()}-{self.lname.lower()}@gmail.com"

    @property
    def mail(self):
        return f"email id is: {self.fname.lower()}-{self.lname.lower()}@gmail.com"

    @property
    def fullname(self): # getter method
        if self.fname is None or self.lname is None:
            return "Name is deleted"
        return f"{self.fname} {self.lname}"
        

    @fullname.setter
    def fullname(self,name): #setter method
        self.fname,self.lname = name.split()
        fullname = self.fname + ' '+self.lname
        return fullname
    
    @fullname.deleter
    def fullname(self): #Deleter method
        self.fname = None
        self.lname = None

# This is a normal way to create an object of a class and call method of that object         
# t1 = Team('Sachin','Tendulkar')
# print(t1.fullname())
# print(t1.mail('Sachin Tendulkar'))


t2 = Team('Virat','Kohli')
print(t2.fullname)
t2.fullname = 'King Kohli'
print(t2.fullname)
print(t2.mail)
time.sleep(3)
print('-'*50)
del t2.fullname
print(t2.fullname)

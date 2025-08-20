from abc import ABC,abstractmethod

class Car(ABC):
    @abstractmethod
    def fuelType(self):
        pass



class Tata:
    def fuelType(self):
        return f"Petrol car"
    
class Maruti:
    def fuelType(self):
        return f"Desel car"
    
t = Tata()
m = Maruti()

print(t.fuelType())
print(m.fuelType())
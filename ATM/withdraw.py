import time
from abc import ABC,abstractmethod
class Payment(ABC):
    @abstractmethod
    def withdraw(self):
        pass

class ATM(Payment):
    __original_pin = 123
    __main_balance = 1000000
    __attampts = 0
    def __init__(self):
        pass
    
    def withdraw(self):
        pin = int(input('Enter your pin:'))
        try:
            if self.__original_pin == pin:
                amount = float(input('Please enter your amount:'))
                print(amount)
                if amount >= self.__main_balance:
                    raise Exception('Insuficient amount')
                else:
                    self.__main_balance = self.__main_balance - amount
                    print(f'available blance is {self.__main_balance}')
            else:
                res = input('Want to try again? (y/n):')
                if res.lower() == 'y':
                    self.__attampts +=1
                    if self.__attampts > 3:
                        print('too may attempts. Your account has been blocked for an hour')
                        time.sleep(3600)
                        return
                    else:
                        self.withdraw()
                else:
                    print('Thank you')
                    return
        except Exception as err:
            print(err)

atm = ATM()
atm.withdraw()
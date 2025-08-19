class Static_method:
    rate_of_inst = 9.45
    @staticmethod
    def interest_calculation(principal,year):
        interest= (principal*year*Static_method.rate_of_inst)
        return interest

print(f"Simpleminterest is: ",Static_method.interest_calculation(100000,5))
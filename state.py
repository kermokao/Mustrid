class CombinationLock:
    def __init__(self, combination):
        self.correct_combination = combination
        self.status = "LOCKED"
        self.entered_digits = []


    def enter_digit(self, digit):
        
        self.entered_digits.append(digit)

        for i in range(len(self.entered_digits)):
            if self.entered_digits[i] != self.correct_combination[i]:
                self.status = "Error"
                return
        
        if len(self.entered_digits) == len(self.correct_combination):
            self.status = "Open"
            return
        
        else:
            self.status = "".join(str(i) for i in self.entered_digits)


cl = CombinationLock([1, 2, 3, 4, 5])
print(cl.status)
 
cl.enter_digit(1)
print(cl.status)
 
cl.enter_digit(2)
print(cl.status)

cl.enter_digit(3)
print(cl.status)

cl.enter_digit(4)
print(cl.status)

cl.enter_digit(5)
print(cl.status)  


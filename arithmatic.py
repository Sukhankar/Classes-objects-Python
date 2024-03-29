class Calculator:
    
    def add(self, x, y):
        return x + y
    
    def mul(self, x, y):
        return x * y
    
    def sub(self, x, y):
        return x - y
    
    def div(self, x, y):
        return x / y
    
    def mod(self, x, y):
        return x % y
    
    def floor(self, x, y):
        return x // y
    
    def exponetion(self, x, y):
        return x ** y

calc = Calculator()

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print(f"{a} + {b} = {calc.add(a, b)}")
print(f"{a} - {b} = {calc.sub(a, b)}")
print(f"{a} * {b} = {calc.mul(a, b)}")
print(f"{a} / {b} = {calc.div(a, b)}")
print(f"{a} % {b} = {calc.mod(a, b)}")
print(f"{a} // {b} = {calc.floor(a, b)}")
print(f"{a} ** {b} = {calc.exponetion(a, b)}")
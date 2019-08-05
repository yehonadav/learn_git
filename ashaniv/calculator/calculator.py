class Calculator:
    answer = None
    def __init__(self, a, b):
        self.a = a
        self.b = b


    def display(self):
        print(self.a)
        print(self.b)
        print(self.answer)

    def add(self):
        Calculator.answer = self.a + self.b

    def sub(self):
        Calculator.answer = self.a - self.b


c = Calculator(2, 8)
c.display()
c.add()
c.display()
c = Calculator(22, 13)
c.sub()
c.display()

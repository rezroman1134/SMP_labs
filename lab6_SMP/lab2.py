import math
class Calculator:
    def __init__(self):
        self.result = None

    def user_input(self):
        number1 = float(input("Enter the first number (the √ is taken from this number): "))
        number2 = float(input("Enter the second number: "))
        operator = input("Enter the operator (+, -, *, /, ^, √, %): ")
        return number1, operator, number2

    def validate_operator(self, operator):
        valid_operators = ['+', '-', '*', '/', '^', '√', '%']
        if operator not in valid_operators:
            print("Error: Invalid operator entered.")
            return False
        return True

    def calculate(self, number1, operator, number2):
        if operator == '+':
            self.result = number1 + number2
        elif operator == '-':
            self.result = number1 - number2
        elif operator == '*':
            self.result = number1 * number2
        elif operator == '/':
            if number2 == 0:
                print("Error: Division by zero is not possible.")
                return
            self.result = number1 / number2
        elif operator == '^':
            self.result = number1 ** number2
        elif operator == '√':
            self.result = math.sqrt(number1)
        elif operator == '%':
            self.result = number1 % number2
        return self.result

    def run_calculator(self):
        while True:
            number1, operator, number2 = self.user_input()
            if not self.validate_operator(operator):
                continue
            self.calculate(number1, operator, number2)
            print(f"Result: {self.result:.2f}")
            choice = input("Do you want to perform another calculation? (y-yes; another symbol-no): ").lower()
            if choice != 'y':
                break

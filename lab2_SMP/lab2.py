import math


# Task 1: Creating the Calculator class
class Calculator:


#Task 2: Initializing the calculator
    def __init__(self):
        self.result = None

#Task3: User input
#Task 10: User-friendly interface
    def user_input(self):
#Task 8: Decimal numbers
        number1 = float(input("Enter the first number (the √ is taken from this number): "))
        number2 = float(input("Enter the second number: "))
        operator = input("Enter the operator (+, -, *, /, ^, √, %): ")
        return number1, operator, number2

#Task4: Operator check
    def validate_operator(self, operator):
        valid_operators = ['+', '-', '*', '/', '^', '√', '%']
        if operator not in valid_operators:
            print("Error: Invalid operator entered.")
            return False
        return True

#Task5: Calculation
    def calculate(self, number1, operator, number2):
        if operator == '+':
            self.result = number1 + number2
        elif operator == '-':
            self.result = number1 - number2
        elif operator == '*':
            self.result = number1 * number2

#Task6: Error handling
        elif operator == '/':
            if number2 == 0:
                print("Error: Division by zero is not possible.")
                return
            self.result = number1 / number2

#Task 9: Additional operations
        elif operator == '^':
            self.result = number1 ** number2

        elif operator == '√':
            self.result = math.sqrt(number1)

        elif operator == '%':
            self.result = number1 % number2

#Task7: Repetition of calculations
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


if __name__ == "__main__":
    calc = Calculator()
    calc.run_calculator()

class Validator:
    def __init__(self, initial_value=None):
        # Your initialization code goes here if needed
        self.initial_value = initial_value

    def validate_input(self, prompt, choices):
        # Utility for validating user input against predefined choices
        while True:
            user_input = input(prompt)
            if choices:
                if user_input in choices:
                    return user_input
                else:
                    print("Invalid choice.")
            else:
                try:
                    return float(user_input)
                except ValueError:
                    print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    # Instantiate Validator with an initial value
    validator = Validator(None)  # You can provide a specific value instead of None
    # Rest of your code...

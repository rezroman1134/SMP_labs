# Importing the ShapeInterface class from the Lb5.Interface module
from Lb5.Interface import ShapeInterface

# Class for running the program and interacting with the user
class Runner:
    def __init__(self):
        # Initializing an instance of the ShapeInterface
        self.interface = ShapeInterface()

    # Main entry point of the program
if __name__ == "__main__":
    # Creating an instance of the Runner class and running the program
    runner = Runner()
    runner.run()

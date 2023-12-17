
from MenuLab8 import MenuLab8

from DataProcessor import DataProcessor
from Validator import Validator
class RunnerLab8:
    @staticmethod

    def run():
        data_processor = DataProcessor()
        validator = Validator(None)
        reader_writer = None
        menu = MenuLab8(data_processor, validator, reader_writer)
        menu.run()


if __name__ == "__main__":
    RunnerLab8.run()

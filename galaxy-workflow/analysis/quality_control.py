"""
The file contains classes and functions for performing quality control
checks on the sequence data

"""
from .galaxy_instance import create_instance  # import the created galaxy instance
from .history import History  # import the history class


class QualityControl:
    """
    The class contains the functions for performing a quality control
    """
    def __init__(self, history_name):
        """
        Initialize the quality control class by:
         a) creating a local class galaxy instance,
         b) creating a local history instance
        """
        self.gi = create_instance()  # create a galaxy instance
        self.history = History().create_history(history_name)  # create a history instance

    def perform_fastqc(self):
        """
        The function performs a fastqc quality check on the sequence data
        :return:
        """
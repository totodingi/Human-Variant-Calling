"""
The file contains functions and classes for operations involving
the galaxy history.

"""
from .galaxy_instance import create_instance


class History:
    """
    this is the history class for manipulating all matters involving
    the galaxy history

    """
    def __init__(self):
        """
        Initialize the history class and create a local class instance of
        the galaxy instance.
        """
        self.gi = create_instance()

    def create_history(self, history_name):
        """
        the function creates a history with the name provided
        :return:
        """
        history = self.fetch_history(history_name)  # get the history if it exists

        if history:
            # if the history with that name exists return it, don't create a new one.
            return history
        else:
            # create a new history
            try:
                # return the history instance if created successfully
                return self.gi.histories.create_history(history_name)
            except NotImplementedError(f"Could not create a history with the {history_name}"):
                pass

        return None  # return a null instance if history not created

    def fetch_history(self, history_name):
        """
        The functions gets the history from the galaxy servers with the name parameter provided

        :param history_name:
        :return:
        """
        try:
            return self.gi.histories.get_histories(name=history_name)  # get a history with the name provided
        except NotImplementedError(f"Could not get a history with the name {history_name}"):
            print("Could not find find history with that name")

        return None

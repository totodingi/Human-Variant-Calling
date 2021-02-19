"""
The file contains classes and functions for performing data operation

"""

from .galaxy_instance import create_instance  # import the galaxy instance


class Data:
    """
    The data class if for handling data operations eg. uploads and downloads
    """

    def __init__(self):
        """
        Initialize the data class
        """
        self.gi = create_instance()  # initialize a galaxy instance


    def upload_data(self, path, history_id, remote=True):
        """
        a function for uploading data either from a remote host or local host
        :param remote:
        :return:
        """
        if remote:
            # executed if the data is remote
            self.gi.tools.upload_from_ftp(path, history_id)
            return True
        else:
            # Executed if the data being uploaded is local
            self.gi.tools.upload_file(path, history_id)
            return True

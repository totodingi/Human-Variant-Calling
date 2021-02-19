"""
The file contains classes and functions for handling the galaxy analysis tools

"""
from .galaxy_instance import create_instance  # import a galaxy instance
from bioblend import toolshed  # imports the toolshed library for accessing the tools


class Tools:
    """
    The class contains functions for getting and manipulating the analysis tools
    """

    def __init__(self):
        """
        Initializes the Tools class and connects to a toolshed instance
        """
        self.gi = create_instance()  # create a galaxy instance.

        self.ts = toolshed.ToolShedInstance(url='https://usegalaxy.eu/')  # create a toolshed instance

    def search_tool(self, tool_name):
        """
        Searches for a tool and returns the tool id
        :return:
        """
        for tool in self.ts.tools.search_tools(tool_name, page_size=1, page=1):
            return tool

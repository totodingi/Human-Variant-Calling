"""
This file is the main entrance to the analysis.

You will require an api key from the galaxy instance you are using.

If you dont have the key yet, please log in into the galaxy portal,
navigate to the user preferences and manage api keys

Copy the API key and copy paste it into a file called a text file in the same directory
as the main.py file.
"""

from analysis.quality_control import QualityControl  # import the quality control class


def main():
    """
    This is the main function that calls other functions and classes in the project.
    :return:
    """
    QualityControl(history_name='Human-Variant-Calling', remote=True, path='http://h3data.cbio.uct.ac.za/assessments/NextGenVariantCalling/practice/H3A_VarCall_TestData.2017.zip')  # call the quality control class.


if __name__ == '__main__':
    # Run the main function
    main()

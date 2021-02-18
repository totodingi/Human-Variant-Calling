"""
This file is the main entrance to the analysis.

You will require an api key from the galaxy instance you are using.

If you dont have the key yet, please log in into the galaxy portal,
navigate to the user preferences and manage api keys

Copy the API key and copy paste it into a file called a text file in the same directory
as the main.py file.
"""

from bioblend.galaxy import GalaxyInstance  # imports the GalaxyInstance class from the bioblend library

# The functions reads the api key stored in a text file and connects to the galaxy server and returns a galaxy instance


def create_instance():
    # Reads the api Key as stored in the text file.
    with open("apikey.txt") as key:
        apikey = key.read()
        key.close()
    # Creates a galaxy instance with the api key provided and the url from the galaxy server
    try:
        gi = GalaxyInstance(url='https://usegalaxy.eu/', key=apikey)
        return gi  # return galaxy instance if connection is successful
    except ConnectionError("Unable to connect to the galaxy servers"):
        pass
    return  # returns a null instance of no connection is made.


def main():
    # The main function that calls other functions in the script.
    create_instance()  # execute the createInstance function


if __name__ == '__main__':
    # Run the main function
    main()

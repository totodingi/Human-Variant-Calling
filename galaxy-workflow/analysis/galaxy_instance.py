"""
The file contains a function that connects to the galaxy servers,
creates an instance and returns it.

"""


from bioblend.galaxy import GalaxyInstance  # imports the GalaxyInstance class from the bioblend library

# The functions reads the api key stored in a text file and connects to the galaxy server and returns a galaxy instance


def create_instance():
    # Reads the api Key as stored in the text file.
    with open("../apikey.txt") as key:
        apikey = key.read()
        key.close()
    # Creates a galaxy instance with the api key provided and the url from the galaxy server
    try:
        gi = GalaxyInstance(url='https://usegalaxy.eu/', key=apikey)
        return gi  # return galaxy instance if connection is successful
    except ConnectionError("Unable to connect to the galaxy servers"):
        pass
    return  # returns a null instance of no connection is made.

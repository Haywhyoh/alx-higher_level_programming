#!usr/bin/python3
""" A python module to do something"""


class Base:
    """A base class for all the other classes
        in this project.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializrion function 
        
            Args:
                id: the in to be returned."""
        if id == None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

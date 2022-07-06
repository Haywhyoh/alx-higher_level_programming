#!/usr/bin/python3
"""A python module for JSON operations."""


class Student:
    """A class to create and manipulate a Student object"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student."""
        if not isinstance(self.attrs, list):
            return self.__dict__

        if not (isinstance(attrs[elem], str) for elem in attrs):
            return self.__dict__
        return({key : value for key, value in self.__dict__.item() 
                if key in attrs})

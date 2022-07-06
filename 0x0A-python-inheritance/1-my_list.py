#!/usr/bin/python3
"""A module that creates myList instance."""


class MyList(list):
    """A class that create a MyList instance.

    Args:
                list - a list object

            Return:
    """

    def print_sorted(self):
        """A method that prints the list, but sorted (ascending sort)

        Args:
            list - a list object

        Return:

        """
        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)

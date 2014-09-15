#!/usr/bin/python

import string
import random


class Namezilla(object):
    """
    A class to generate random names
    """
    OPTION_TYPES = ['1', '2', '3']
    MIN_LENGTH = 3
    MAX_LENGTH = 8

    def __init__(self):
        pass

    def __str__(self):
        return "\nThe name is: %s\n" % self._name

    @property
    def name(self):
        """
        Getter method for name
        """
        return self._name

    @property
    def option(self):
        """
        Getter method for option
        """
        return self._option

    def render_options(self):
        """
        Displays the options
        """
        print "\nWelcome to namezilla"
        print "---------------------"
        print "Do you want to generate a new name?\n"
        print "Options:\n"
        print "(1) Personal name"
        print "(2) Group name"
        print "(3) Company name"
        print ".. or another key to exit"

    def render_repeater(self):
        """
        Checks if the user wants to repeat the process
        """
        input_option = raw_input(
            "Press 1 to repeat or another key to exit..")
        if input_option != '1':
            print "Exiting.."

        return True if input_option == '1' else False

    def capture_option(self):
        """
        Captures the selected option
        """
        input_option = raw_input(
            "\nPress Enter an option to continue...")
        self._option = int(input_option) \
            if input_option in self.OPTION_TYPES else 0

    def generate_name(self):
        """
        Produces a name based on the property option
        """

        random_length = random.randint(self.MIN_LENGTH, self.MAX_LENGTH)
        random_str = self.get_random_str(random_length)

        if self._option == 1:
            self._name = "Mr %s" % random_str.title()
        elif self._option == 2:
            self._name = "%s Group" % random_str.title()
        elif self._option == 3:
            self._name = "%s Ltd" % random_str.title()

    @classmethod
    def get_random_str(cls, nlength):
        """
        Returns a random string based on the n lenght param

        :n: Length of the output string
        """
        return ''.join(
            random.choice(string.ascii_uppercase) for _ in range(nlength))

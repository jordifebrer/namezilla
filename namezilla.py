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

        print "\nWelcome to namezilla"
        print "---------------------"
        print "Do you want to generate a new name?\n"
        print "Options:\n"
        print "(1) Personal name"
        print "(2) Group name"
        print "(3) Company name"
        print ".. or another key to exit"

        option = self._check_option()
            
        if option > 0:
            name = self._do_name(option)
            print "The name is: %s\n" % name
            
            if (self._check_repeat()): 
                self.__init__()
        
        else:
            print "Exiting.."


    def _check_option(self):
        """
        Checks for the validity of the selected option 
        """
        input_option = raw_input(
            "\nPress Enter an option to continue...")
        return int(input_option) if input_option in self.OPTION_TYPES else 0


    def _check_repeat(self):
        """
        Checks if the user wants to generate a new name or not
        """
        input_option = raw_input(
            "Press 1 to repeat or another key to exit..")
        return True if input_option == '1' else False


    def _do_name(self, option):
        """
        Produces a name based on the selected option

        :option: Type of name
        """
        out = ""
        random_length = random.randint(self.MIN_LENGTH, self.MAX_LENGTH)
        random_str = self._get_random_str(random_length)

        if option == 1:
            out = "Mr %s" % random_str.title()
        elif option == 2:
            out = "%s Group" % random_str.title()
        elif option == 3:
            out = "%s Ltd" % random_str.title()

        return out


    def _get_random_str(self, n):
        """
        Returns a random string based on the n lenght param

        :n: Length of the output string
        """
        return ''.join(
            random.choice(string.ascii_uppercase) for _ in range(n))


name = Namezilla()

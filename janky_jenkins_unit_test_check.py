import sys
import unittest

debug = "yes"

class TestStrings(unittest.TestCase):

    param = str(sys.argv[1])

    print ("Script name is: ", param)

    #Getter: Prompt user for input, return input

    def test_Input(self):
        print ("Please type yes to answer the question correctly")
        inp = str(debug)
        self.assertEqual(inp,"yes")
        print("You entered: ", inp)

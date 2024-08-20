import unittest  # Importing the unittest module, which provides classes and functions for writing and running tests

# Defining a simple function 'add' that takes two arguments x and y and returns their sum
def add(x, y):
    return x + y

# Creating a test class named 'TestNumber' that inherits from unittest.TestCase
# This class will contain the test cases for the 'add' function
class TestNumber(unittest.TestCase):
    
    # Defining a test method 'test_add' to test the 'add' function
    # The method uses 'assertEqual' to check if the output of 'add' is as expected
    def test_add(self):
        self.assertEqual(add(3, 2), 5)  # Test if add(3, 2) returns 5
        self.assertEqual(add(-1, 1), 0)  # Test if add(-1, 1) returns 0
        self.assertEqual(add(2, 3), 6)  # Test if add(2, 4) returns 6

# If this script is run directly, the following block will execute
# 'unittest.main()' is called to run the tests defined in the TestNumber class
if __name__ == '__main__':
    unittest.main()

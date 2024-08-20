import unittest  # Importing the unittest module, which is Python's standard library for unit testing [1]

class TestApi(unittest.TestCase):  # Defining a test class named TestApi that inherits from unittest.TestCase [2]
    
    def test_1(self):
        print("Hello world")  # Test case that prints "Hello world" to the console [3]
    
    def test_2(self):
        print("HAPPY TIME")  # Test case that prints "HAPPY TIME" to the console [4]

if __name__ == '__main__':
    unittest.main()  # Launching the unittest framework, which automatically runs all methods that start with 'test' [5]

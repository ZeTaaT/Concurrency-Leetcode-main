import unittest
from unittest import IsolatedAsyncioTestCase
from os.path import exists
from Producer import Producer

#Testing all the processes in the project

class TestStringMethods(unittest.TestCase): 

    #Checks if the fake file exists in the current context
    def test_test_file_exists(self): 
        dataPath = "../fakeData/testData1.txt"
        self.assertTrue(exists(dataPath)) 


    #Checks if the test file exists in the current context
    def test_fake_file_exists(self): 
        dataPath = "../fakeData/fakeData1.txt"
        self.assertTrue(exists(dataPath)) 


if __name__ == '__main__':
    unittest.main() 
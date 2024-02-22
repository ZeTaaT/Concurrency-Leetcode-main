import unittest
from os.path import exists

#Testing all the processes in the project

class TestStringMethods(unittest.TestCase): 
      
    def setUp(self): 
        pass
  
    #Checks if the file exists in the current context
    def test_file_exists(self): 

        dataPath = "../fakeData/fakeData1.txt"
        self.assertEqual(exists(dataPath), True) 

    def 


if __name__ == "__main__":
    unittest.main() 
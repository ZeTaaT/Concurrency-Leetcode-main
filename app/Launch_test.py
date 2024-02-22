import unittest
from os.path import exists

#Testing all the processes in the project

class TestStringMethods(unittest.TestCase): 
      
    def setUp(self): 
        pass
  
    #Checks if the file exists in the current context
    def test_files_exist(self): 
        dataPath = "../fakeData/fakeData1.txt"
        
        self.assertEqual(exists(dataPath), True) 


if __name__ == "__main__":
    unittest.main() 
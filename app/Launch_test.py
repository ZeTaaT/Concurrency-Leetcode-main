import unittest
from unittest import IsolatedAsyncioTestCase
from os.path import exists
from Producer import Producer

#Testing all the processes in the project

events=[]

class Test(IsolatedAsyncioTestCase): 
      
    def setUp(self): 
        events.append("setUp")
        pass

    #Checks if the fake file exists in the current context
    def test_test_file_exists(self): 
        dataPath = "../fakeData/testData1.txt"
        self.assertEqual(exists(dataPath), True) 


    #Checks if the test file exists in the current context
    def test_fake_file_exists(self): 
        dataPath = "../fakeData/fakeData1.txt"
        self.assertEqual(exists(dataPath), True) 

    async def test_producer_works(self):
        events.append("test_response")
        dataPath = "../fakeData/testData1.txt"
        test_prod = Producer()
        await test_prod.startWorking(dataPath)
        self.assertEqual(not test_prod.queueHtml.empty(), True) 


if __name__ == "__main__":
    unittest.main() 
import unittest
from unittest import IsolatedAsyncioTestCase
from os.path import exists
from Producer import Producer
from Consumer import Consumer

#Testing all the processes in the project

class Test(IsolatedAsyncioTestCase): 
      
    def setUp(self): 
        pass

    #Checks if the fake file exists in the current context
    def test_test_file_exists(self): 
        dataPath = "../fakeData/testData1.txt"
        self.assertEqual(exists(dataPath), True) 


    #Checks if the test file exists in the current context
    def test_fake_file_exists(self): 
        dataPath = "../fakeData/fakeData1.txt"
        self.assertEqual(exists(dataPath), True) 

    async def test_producer_consumer_works(self):
        dataPath = "../fakeData/testData1.txt"
        test_prod = Producer()
        test_cons = Consumer()
        await test_prod.startWorking(dataPath)
        await test_cons.startWorking(test_prod, False)
        self.assertEqual(test_prod.queueHtml.empty(), True) 
        self.assertEqual(len(test_cons.htmlDequeue) == 0, True) 


if __name__ == "__main__":
    unittest.main() 
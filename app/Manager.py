from Producer import Producer
from Consumer import Consumer

class Manager:

    dataPath = "fakeData1.txt"

    cons1 = Consumer()
    prod1 = Producer()

    def __init__(self, cons: Consumer, prod: Producer, dataPath: str): #Constructor
        self.dataPath = dataPath
        self.cons1 = cons
        self.prod1 = prod
    

    def Launch(self):
        print("Started Manager")
        self.prod1.startWorking(self.dataPath)
        self.cons1.startWorking(self.prod1)

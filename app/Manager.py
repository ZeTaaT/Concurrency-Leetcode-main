from Producer import Producer
from Consumer import Consumer

import asyncio

class Manager:

    dataPath = "fakeData.txt"

    cons1 = Consumer()
    prod1 = Producer()

    def __init__(self, cons: Consumer, prod: Producer, dataPath: str): #Constructor
        self.dataPath = dataPath
        self.cons1 = cons
        self.prod1 = prod
    

    async def Launch(self):
        print("Started Manager")
        
        await self.prod1.startWorking(self.dataPath)
        await self.cons1.startWorking(self.prod1)

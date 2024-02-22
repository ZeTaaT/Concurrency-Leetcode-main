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
    
    async def scream(self):
        while True:
            await self.cons1.startWorking(self.prod1)

    async def shout(self):
        await self.prod1.startWorking(self.dataPath)
    
    async def Launch(self):
        print("Started Manager")
        task = asyncio.create_task(self.scream())
        await self.shout()

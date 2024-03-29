from app.Producer import Producer
from app.Consumer import Consumer
import asyncio

class Manager: #Manage Producer and Consumer

    dataPath = "../fakeData/fakeData1.txt"

    cons1 = Consumer()
    prod1 = Producer()

    def __init__(self, cons: Consumer, prod: Producer, dataPath: str): #Constructor
        self.dataPath = dataPath
        self.cons1 = cons
        self.prod1 = prod
    
    async def consumerTask(self):
        while True:
            await self.cons1.startWorking(self.prod1)
    
    async def Launch(self):
        print("Started Manager")
        task = asyncio.create_task(self.consumerTask())
        await self.prod1.startWorking(self.dataPath)

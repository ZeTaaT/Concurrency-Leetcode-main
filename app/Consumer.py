from collections import deque
from bs4 import BeautifulSoup
from Producer import Producer

import asyncio

class Consumer: #Extract keypoint from HTML data
    dataQueue = deque()

    def __init__(self):
        self.dataQueue = deque() #good way of storing data as queue

    async def readQueue(self, prod: Producer): #Read the queue of urls and htmls
        dataQueue = prod.queueData
        try:
            while not dataQueue.empty():
                data = dataQueue.get()
                self.dataQueue.append((await self.extractHyper(data[1]), data[0]))


                #self.dataQueue.append(await self.extractHyper(dataQueue.get()), )
                #self.urlDequeue.append(queueUrl.get())
            await asyncio.sleep(0.001)
        except Exception as e:
            print("Error while adding hyperlinks", e)


    async def extractHyper(self, soup: BeautifulSoup): #Extract needed element, in this case hyperlinks
        listHyper = []
        try:
            for link in soup.find_all('a'): 
                listHyper.append(link.get('href'))
            return listHyper
        except Exception as e:
            print("Error while extracting hyperlinks", e)


    async def startWorking(self, prod: Producer, printStuff: bool = True): #Start the Consumers
        await self.readQueue(prod) #Read the queue of the producer
        if(printStuff): #Print out all objects in queues
            while len(self.dataQueue):
                data = self.dataQueue.pop()
                print(data[1])
                print(data[0])
        else: #Empty queues
            while len(self.dataQueue):
                self.dataQueue.pop()
        


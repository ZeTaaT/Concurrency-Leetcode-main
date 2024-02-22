from collections import deque
from bs4 import BeautifulSoup
from Producer import Producer
from queue import Queue

import asyncio
class Consumer:

    htmlDequeue = deque() #queue for html
    urlDequeue = deque() #queue for url

    def __init__(self):
        self.htmlQueue = deque() #good way of storing data as queue

    async def readQueue(self, prod: Producer):
        print("Consumer reading the queue")
        queueHtml = prod.queueHtml
        queueUrl = prod.queueUrl
        while not queueHtml.empty():
            self.htmlDequeue.append(await self.extractHyper(queueHtml.get()))
            self.urlDequeue.append(queueUrl.get())
        print("Queue is empty")
        await asyncio.sleep(1)


    async def extractHyper(self, soup: BeautifulSoup):
        listHyper = []
        try:
            for link in soup.find_all('a'): 
                listHyper.append(link.get('href'))
            return listHyper
        except Exception as e:
            print("Error while extracting hyperlinks" + e)


    async def startWorking(self, prod: Producer):
        print("Consumer is getting the stuff")
        await self.readQueue(prod)
        while len(self.htmlDequeue):
            print(self.urlDequeue.pop())
            print(self.htmlDequeue.pop())


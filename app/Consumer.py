from collections import deque
from bs4 import BeautifulSoup
from app.Producer import Producer
from queue import Queue

import asyncio
class Consumer:

    htmlDequeue = deque() #queue for html
    urlDequeue = deque() #queue for url

    def __init__(self):
        self.htmlQueue = deque() #good way of storing data as queue

    async def readQueue(self, prod: Producer):
        queueHtml = prod.queueHtml
        queueUrl = prod.queueUrl
        try:
            while not queueHtml.empty():
                self.htmlDequeue.append(await self.extractHyper(queueHtml.get()))
                self.urlDequeue.append(queueUrl.get())
            await asyncio.sleep(0.001)
        except Exception as e:
            print("Error while adding hyperlinks" + e)


    async def extractHyper(self, soup: BeautifulSoup):
        listHyper = []
        try:
            for link in soup.find_all('a'): 
                listHyper.append(link.get('href'))
            return listHyper
        except Exception as e:
            print("Error while extracting hyperlinks" + e)


    async def startWorking(self, prod: Producer, printStuff: bool = True):
        await self.readQueue(prod)
        if(printStuff):
            while len(self.htmlDequeue):
                print(self.urlDequeue.pop())
                print(self.htmlDequeue.pop())
        else:
            while len(self.htmlDequeue):
                self.urlDequeue.pop()
                self.htmlDequeue.pop()
        


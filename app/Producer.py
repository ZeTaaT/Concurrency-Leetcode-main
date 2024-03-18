from queue import Queue
from bs4 import BeautifulSoup
import requests 

import asyncio

class Producer: #Collect Html data
    queueData: Queue

    def __init__(self): #Constructor
        self.queueData = Queue(maxsize=10000) #queue from queue are more effecient than deque becuase of threading communications, although am not using threads

    async def readURL(self, dataPath: str): #read URLs from the list file
        try:
            with open(dataPath, 'r') as file:
                for url in file:
                    url = url.strip() #Strip for the empty spaces
                    await self.extractMarkup(url)
        except Exception as e:
            print("Error while reading data", e) #Thrown when the file doesn't exist

    async def requestHTML(self, url: str) -> requests.Response: #Get HTML from the URL
        try:
            response = requests.get(url, timeout = 1) 
            return response
        except Exception as e: 
            print("Error while getting html:", e)
            response = requests.Response()
            response.status_code = 500
            response._content = ""
            response.reason = e
            return response


    async def makeSoup(self, html_document: requests.Response): #Make the HTML into a soup(More ordered HTML that is used in the future to sort out markups)
        try:
            return BeautifulSoup(html_document.content, 'html.parser') 
        except Exception as e:
            print("Error while making soup:", e)
            return BeautifulSoup("", "html.parser")
        
    async def extractMarkup(self, url: str): #Extract Markup from the URL.
        html_document = await self.requestHTML(url)
        if(html_document.ok):
            soup = await self.makeSoup(html_document)
            self.queueData.put((url, soup)) #Even if the HTML empty, put html into a queue as well as the url it was taken from
        await asyncio.sleep(0.001)

    async def startWorking(self, dataPath: str): #Start the Producer
        await self.readURL(dataPath)
        print("Finished working", self.queueData.qsize())


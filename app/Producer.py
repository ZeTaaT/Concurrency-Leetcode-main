from queue import Queue
from bs4 import BeautifulSoup
import requests 

import asyncio

class Producer:
    queueHtml = Queue()
    queueUrl = Queue()

    def __init__(self): #Constructor
        self.queue = Queue(maxsize=10000) #queue from queue are more effecient than deque becuase of threading communications

    async def readURL(self, dataPath: str): #read URLs from the list file

        try:
            file = open(dataPath, 'r')
            while file:
                url = file.readline().strip() #Strip for the empty spaces
                if url == "": #If list is empty exit
                    break
                else:
                    await self.extractMarkup(url)
            file.close()
        except Exception as e:
            print("Error while reading data" + e)

    async def requestHTML(self, url: str): #Get HTML from the URL
        try:
            response = requests.get(url) 
            if response.status_code == 200:
                return response
            elif response.status_code == 404:
                return ""
        except Exception as e:
            print("Error while fetching website HTML:", e)
            return ""

    async def makeSoup(self, html_document): #Make the HTML into a soup(More ordered HTML that is used in the future to sort out markups)
        try:
            soup = BeautifulSoup(html_document.content, 'html.parser') 
            return soup
        except Exception as e:
            print("Error while making soup:", e)
            return ""
        
    async def extractMarkup(self, url: str): #Extract Markup from the URL.
        html_document = await self.requestHTML(url)
        soup = await self.makeSoup(html_document)
        if(soup != ""):
            self.queueHtml.put(soup)
            self.queueUrl.put(url)
        await asyncio.sleep(0.001)

    async def startWorking(self, dataPath: str):
        await self.readURL(dataPath)
        print("Finished working", self.queueHtml.qsize())


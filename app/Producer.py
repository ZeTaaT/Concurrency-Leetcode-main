from queue import Queue
from bs4 import BeautifulSoup
import requests 
import re 

class Producer:
    queue = Queue()

    def __init__(self): #Constructor
        self.queue = Queue(maxsize=10000) #queue from queue are more effecient than deque becuase of threading communications

    def readURL(self, dataPath: str): #read URLs from the list file

        print("Trying to read the data")
        try:
            file = open(dataPath, 'r')
            url = file.readline().strip() #Strip for the empty spaces
            print(url)
            return url
        except Exception as e:
            print("Error while reading data" + e)

    def requestHTML(self, url: str):
        try:
            response = requests.get(url) 

            if response.status_code == 200:
                print('Success!')
            elif response.status_code == 404:
                print('Not Found.')

            return response
        except Exception as e:
            print("Error while fetching website HTML:", e)

    def makeSoup(self, html_document):
        try:
            soup = BeautifulSoup(html_document.content, 'html.parser') 
            for link in soup.find_all('a',  
                          attrs={'href': re.compile("^https://")}): 
                # display the actual urls 
                print(link.get('href'))   
        except Exception as e:
            print("Error while making soup:", e)
        
    def extractMarkup(self, url: str): #Extract Markup from the queue. wtf is a markup?
        html_document = self.requestHTML(url)
        self.makeSoup(html_document)

    def startWorking(self, dataPath: str):
        url = self.readURL(dataPath)
        self.extractMarkup(url)
        

from queue import Queue
from bs4 import BeautifulSoup
import requests 

class Producer:
    queue = Queue()

    def __init__(self): #Constructor
        self.queue = Queue(maxsize=10000) #queue from queue are more effecient than deque becuase of threading communications

    def readURL(self, dataPath: str): #read URLs from the list file

        print("Trying to read the data")
        try:
            file = open(dataPath, 'r')
            while file:
                url = file.readline().strip() #Strip for the empty spaces
                if url == "":
                    break
                else:
                    self.extractMarkup(url)
            file.close()
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
            return ""

    def makeSoup(self, html_document):
        try:
            soup = BeautifulSoup(html_document.content, 'html.parser') 
            print(soup)
            #for link in soup.find_all('a'): 
            #    print(link.get('href'))   
            return soup
        except Exception as e:
            print("Error while making soup:", e)
            return ""
        
    def extractMarkup(self, url: str): #Extract Markup from the URL. wtf is a markup?
        html_document = self.requestHTML(url)
        soup = self.makeSoup(html_document)
        self.queue.put(soup)

    def startWorking(self, dataPath: str):
        self.readURL(dataPath)
        print("Finished working", self.queue.qsize())


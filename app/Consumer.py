from collections import deque
from bs4 import BeautifulSoup
from Producer import Producer
from queue import Queue
class Consumer:

    htmlQueue = deque()

    def __init__(self):
        self.htmlQueue = deque() #good way of storing data as queue

    def readQueue(self, queue: Queue):
        while not queue.empty():
            self.htmlQueue.append(self.extractHyper(queue.get()))
        print("code")

    def extractHyper(self, soup: BeautifulSoup):
        for link in soup.find_all('a'): 
           print(link.get('href'))   

    def startWorking(self, prod: Producer):
        self.readQueue(prod.queue)

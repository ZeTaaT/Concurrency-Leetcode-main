from collections import deque
from Producer import Producer
class Consumer:

    htmlQueue = []

    def __init__(self):
        self.htmlQueue = deque() #good way of storing data as queue

    def readQueue(self):
        print("code")

    def startWorking(self, prod: Producer):
        print("AAAAA")

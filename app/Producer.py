from queue import Queue

class Producer:
    queue = Queue()

    def __init__(self): #Constructor
        self.queue = Queue(maxsize=10000) #queue from queue are more effecient than deque becuase of threading communications

    def readURL(self, dataPath: str): #read URLs from the list file
        print("Trying to read the data")
        try:
            file = open(dataPath, 'r')
            url = file.readline()
            return url
        except Exception as e:
            print(e)

    def extractMarkup(self, url: str): #Extract Markup from the queue. wtf is a markup?
        
        print(url)

    def startWorking(self, dataPath: str):
        url = self.readURL(dataPath)
        self.extractMarkup(url)
        

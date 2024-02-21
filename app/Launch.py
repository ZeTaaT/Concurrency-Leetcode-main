from Manager import Manager
from Producer import Producer
from Consumer import Consumer


def main():
    
    dataPath = "../fakeData/fakeData1.txt"
    cons1 = Consumer()
    prod1 = Producer()
    manager = Manager(cons1, prod1, dataPath)
    try:
        print("Starting Manager")
        manager.Launch()
    except Exception as e:
        print(e)

main()
from Manager import Manager
from Producer import Producer
from Consumer import Consumer
import asyncio


async def main():
    
    dataPath = "../fakeData/fakeData1.txt"
    cons1 = Consumer()
    prod1 = Producer()
    manager = Manager(cons1, prod1, dataPath)
    try:
        print("Starting Manager")
        await manager.Launch()
        print("Manager managed the job")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
import asyncio
import time


async def myWorker(lock):
    # with await lock:
    print("myWorker has attained lock, modifying variable")
    time.sleep(2)
    print("myWorker has release the lock")


async def main():
    lock = asyncio.Lock()
    await asyncio.wait([myWorker(lock), myWorker(lock)]),


loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()

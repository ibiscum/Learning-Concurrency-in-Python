import asyncio
import random


# @asyncio.coroutine
async def newsProducer(my_queue):
    while True:
        my_queue.put(random.randint(1, 5))
        # asyncio.sleep(1)


@asyncio.coroutine
def newsConsumer(myQueue):
    while True:
        articleId = yield from myQueue.get()
        print("News Reader Consumed News Article {}", articleId)


myQueue = asyncio.Queue()

loop = asyncio.get_event_loop()

loop.create_task(newsProducer(myQueue))
loop.create_task(newsConsumer(myQueue))

try:
    loop.run_forever()
finally:
    loop.close()

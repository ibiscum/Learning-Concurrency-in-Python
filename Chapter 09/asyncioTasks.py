import asyncio


async def my_coroutine():
    print("My Coroutine")


async def main():
    await asyncio.sleep(1)


loop = asyncio.get_event_loop()
try:
    loop.create_task(my_coroutine())
    loop.create_task(my_coroutine())
    loop.create_task(my_coroutine())

    pending = asyncio.Task.all_tasks()
    print(pending)
    loop.run_until_complete(main())
finally:
    loop.close()

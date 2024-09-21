"""
                asynico实现协程
"""
import asyncio


async def worker_a():
    print('start worker a')
    await asyncio.sleep(2)
    print('end worker a')


async def worker_b():
    print('start worker b')
    await asyncio.sleep(3)
    print('end worker b')


cor_a = worker_a()
cor_b = worker_b()
tasks = [asyncio.ensure_future(cor_a), asyncio.ensure_future(cor_b)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))


# 此处报错为DeprecationWarning，意为现在的版本可用，以后版本可能出错

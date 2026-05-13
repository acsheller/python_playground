import asyncio


async def worker(name):
    for i in range(5):
        print(f"{name}: {i}")
        await asyncio.sleep(1)


async def main():
    await asyncio.gather(
        worker("alpha"),
        worker("beta"),
    )


asyncio.run(main())
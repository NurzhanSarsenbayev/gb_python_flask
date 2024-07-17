import asyncio

async def count():
    print('Start')
    await asyncio.sleep(1)
    print('1 second passed')
    await asyncio.sleep(2)
    print('2 second passed')
    return 'End'

async def main():
    result = await asyncio.gather(count(), count(), count())
    print(result)

asyncio.run(main())
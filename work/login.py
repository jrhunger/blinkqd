import asyncio
from aiohttp import ClientSession
from blinkpy.blinkpy import Blink

async def start():
    session = ClientSession()
    blink = Blink(session=session)
    await blink.start()
    await blink.save("/work/creds.json")
    await session.close()
    return blink

blink = asyncio.run(start())


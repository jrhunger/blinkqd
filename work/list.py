import asyncio
from aiohttp import ClientSession
from blinkpy.blinkpy import Blink
from blinkpy.auth import Auth
from blinkpy.helpers.util import json_load
import logging
import sys

blog = logging.getLogger('blinkpy')
blog.setLevel(logging.DEBUG)
bhand = logging.StreamHandler(sys.stderr)
bhand.setLevel(logging.DEBUG)
bform = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
bhand.setFormatter(bform)
blog.addHandler(bhand)

async def start(session: ClientSession):
    blink = Blink(session=session)
    blink.auth = Auth(await json_load("/work/creds.json"), session=session)
    await blink.start()
    return blink

async def list_cameras(blink):
  for name, camera in blink.cameras.items():
    print(name)                   # Name of the camera
    print(camera.attributes)      # Print available attributes of camera

async def main():
    session = ClientSession()
    blink = await start(session)
    await list_cameras(blink)
    await blink.save("/work/creds.json")
    await session.close()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

import websockets
import asyncio
from datetime import datetime
import time

async def socketsHandler(websocket):
    client = "0.0.0.0"
    try:
        client = websocket.remote_address[0]
        print ("Client connected from " + client)
        while True:
            await websocket.send(str(datetime.now()))
            time.sleep(1)
    except Exception as e:
        print (str(e))
        print ("Connection lost: " + str(client))

async def main():
    async with websockets.serve(socketsHandler, "0.0.0.0", 8082):
        await asyncio.Future()

print ("Started!")
asyncio.run(main())
import websockets
import asyncio

async def user():
    # `ws://localhost:8000/ws/${client_id}`);
    url='ws://localhost:8000'
    async with websockets.connect(url) as ws:
        print("connected")
        k='123'
        await ws.send(k)
        msg=await ws.recv()
        strings=str(msg).split()
        print(strings[0])
        if strings[0]=='ok':
            while True:
                j=input("ques : ")
                await ws.send(str(k)+" "+str(j))
                while True:
                    msg=await ws.recv()
                    break
                print(msg)
        ws.close()

try:
    print('Start connecting')
    asyncio.get_event_loop().run_until_complete(user())
    print('Connection lost')
except:
    print("Connection Falied")
